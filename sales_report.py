"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
#declares a variable for salespeople
melons_sold = []
#declares a variable for melons_sold

f = open('sales-report.txt')
#opens the sales-report.txt file

for line in f: 
#loops over each line in the file
    line = line.rstrip() 
    #removes whitespace
    entries = line.split('|') 
    #splits at the "|"

    salesperson = entries[0] 
    #get a name of a salesperson
    melons = int(entries[2]) 
    #get the amount of melons sold

    if salesperson in salespeople:
    #checks to see if the salesperson is already in salespeople
        position = salespeople.index(salesperson)
        #looks at the index of the salesperson and assigns it to the variable position
        melons_sold[position] += melons
        # increment the number of melons the salesperson sold.
    else:
    #if no salesperson is found, the else statement will run
        salespeople.append(salesperson)
        # Else add the salesperson's name to salespeople
        melons_sold.append(melons)
        # add melons to `melons_sold`


for i in range(len(salespeople)):
#iterate over the length of salespeople
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
    #print the statement with their name and melon units they sold.