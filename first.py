import xlsxwriter

workbook = xlsxwriter.Workbook("/home/hamid/Documents/Excle/test.xlsx")

worksheet = workbook.add_worksheet('My_Test')


x = [2,4,6,8,10]
y = 0

for i in range(5):
    worksheet.write(i,y,x[i-1])

l = len(x)+1
worksheet.write(l,y,'=SUM(A1:A5)')

# worksheet.write('A1','Hamid')
# worksheet.write(1,0,'Hassan')

workbook.close();