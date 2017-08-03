#! python3
#generates pseudorandom list of wroking days
#
import xlsxwriter
import itertools
import random

# creates excel workbook
workbook = xlsxwriter.Workbook('filename.xlsx')
worksheet = workbook.add_worksheet()

#generator of workdays by itertools
result = itertools.cycle([8, 8, 8, 8, 8, u'B', u'B'])

#input number of raws
rows = int(input('input number of rows  '))

#Creates list of working days 200 items long
mylist = []
for l in range(200):
    mylist.append(next(result))

##print(mylist,end='\n')
##print('\n')

'''
generates slice from list of items with random start number
and writes it to workbook by rows and columns
'''
for row in range(rows):
    randint = random.randint(5, 20)
    slice = list(mylist[randint:randint+30])

    for column in range(21):
##        print('item in slice {0} index in slice {1}'.format(slice[j],j))
        worksheet.write(row, column, slice[column])
        if rows == 0:
            print('break')
            break
    rows -= 1

workbook.close()
