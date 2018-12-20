Created on Wed Dec 19 22:37:08 2018

@author: kq
"""
import xlsxwriter
workbook = xlsxwriter.Workbook('chart_data_table.xlsx') #可以生成.xls文件但是会报错
worksheet = workbook.add_worksheet('Sheet1') #工作页
#bold = workbook.add_format({'bold': 1})
headings = ['Number', 'Batch 1', 'Batch 2']
data = [
  [10, 40, 50, 20, 10, 50],
  [10, 40, 50, 20, 10, 50],
  [30, 60, 70, 50, 40, 30],
]
#插入数据
worksheet.write_row('A1', headings)#行插入操作 注意这里的'A1'
worksheet.write_column('A2', data[0])#列插入操作 注意这里的'A2'
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])

workbook.close()
