import csv

with open(<filename>) as csv_file:
	csv_reader = csv.reader(csv_file)
    
    #next(csv_reader)#moves the cursor to the 2nd line - column will be skipped by this action
    
    with open() as new_file:
        csv_writer = csv.writer(new_file,delimiter='-')
        for line in csv_reader:
            csv_writer.writerow(line)
            

#DictReader and DictWriter can be used instead of regular reader and writer - where lines will be of dict format instead of list in default case

with open(<filename>) as csv_file:
	csv_reader = csv.Dictreader(csv_file)
    
    #next(csv_reader)#moves the cursor to the 2nd line - column will be skipped by this action
    
    with open() as new_file:
        filednames = ['firstname','lastname','email']
        csv_writer = csv.Dictwriter(new_file,filednames=filednames,delimiter='-')
        csv_writer.writeheader()# to have columns included in the result csv
        for line in csv_reader:
            csv_writer.writerow(line)
            
            
###use case1
##to have only first name and last name, no need of email
with open(<filename>) as csv_file:
	csv_reader = csv.Dictreader(csv_file)
    
    #next(csv_reader)#moves the cursor to the 2nd line - column will be skipped by this action
    
    with open() as new_file:
        filednames = ['firstname','lastname']
        csv_writer = csv.Dictwriter(new_file,filednames=filednames,delimiter='-')
        csv_writer.writeheader()# to have columns included in the result csv
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)