from openpyxl import Workbook
book=Workbook()
sheet=book.active
sheet['A1']='RollNumber'
sheet['B1']='Stude Name'
sheet['a2']='101'
sheet['b2']="kiran"
book.save("date.xlsx")
