from optparse import Values


data = open('./CupcakeInvoices.csv')

# for row in data:
#     print(row)

# for row in data:
#     values = row.split(',')
#     print(values[2])

# for row in data:
#     values = row.split(',')
#     total = int(values[3]) * float(values[4])
#     print(total) 


total = 0

for row in data: 
    values = row.split(',')
    total = total + int(values[3]) * float(values[4])
    
print(total)

data.close()