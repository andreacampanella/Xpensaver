import csv
import sys, getopt

def main(argv):
    inputfile = ''
    month = ''
   
    try:
        opts, args = getopt.getopt(argv,"hi:m:",["ifile=","month="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -m month'
        sys.exit(2)
   
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -m month'
            sys.exit()

        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-m", "--month"):
            month = arg


    print 'Input file is ', inputfile
    print 'Month is ', month


    with open(inputfile, 'rb') as csvfile_input:
        csvfile_input = csv.reader(csvfile_input, delimiter=',',)

        total = 0.0 
        i = 0 

        dbfile = [{"Memo": "", "Ammount": 0.0}]
        for row in csvfile_input: 
            #Number,Date,Account,Amount,Subcategory,Memo

            if(str(row[0]) != "Number"):
                #print row
                found = 0 
                memo = row[5][:7]
                ammount = float(row[3])
                
                if int(row[1][3:5]) == int(month) :              
                    for line in xrange(0,len(dbfile)):
                        #search the db for a new entry
                        if  dbfile[line]["Memo"] ==  memo:
                            dbfile[line]["Ammount"] = dbfile[line]["Ammount"] + ammount
                            found = 1           
                    if line == len(dbfile) -1 and found == 0:
                        #if the entry is not there, add it.
                        dbfile.append({"Memo": memo, "Ammount":ammount})
                

        for line in dbfile:
            print line["Memo"]+","+"{0:.2f}".format(line["Ammount"])
            total = total + line["Ammount"]
        print "Total:"
        print  total






if __name__ == "__main__":
   main(sys.argv[1:])
