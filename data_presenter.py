# Open the CupcakeInvoices.csv.
open_file = open("CupcakeInvoices.csv")

# Loop through all the data and print each row.
# for line in open_file:
#     print(line)

# Loop through all the data and print the type of cupcakes purchased.
# for line in open_file:
#     line = line.split(",") # split by comma => output is an Array
#     print(line[2]) # bracket notation to access value
  
# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
# for line in open_file:
#     line = line.rstrip('\n').split(",") # split by comma => output is an Array
#     print(line[4])
# Loop through all the data, and print out the total for all invoices combined.
combined_invoices = 0
for line in open_file:
    line = line.rstrip('\n').split(",") # split by comma => output is an Array
    num = line[4] # the value at this line is a string
    float_num = float(num) # convert the string to a float variable (this is because of decimal mark)
    int_num = int(float_num) # now that it is float, in order to have an interger we need to convert it to an integer
    combined_invoices += int_num # now that that we have an integer we can increment out 'int_num' variable to 'combine_invoices'
print(combined_invoices)
# Close your open file.
# open_file.close()