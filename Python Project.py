import pandas as pd
import numpy as np

print('Usecase-1 Load All three Csv dataset in Pandas DataFrame and display first five Record')
customers_column = ['custno','firstname','lastname','gender','age','profession','contactNo','emailId','city','state','isActive ','createdDate','UpdatedDate']
df_cust = pd.read_csv(r'C:\Users\Admin\Downloads\Data thecnogeeks\Data_Engineering\PythonProject\CSV_s1\customers.csv',header=None,names=customers_column)
print(df_cust.head())
products_column = ['productno','productName','Description','isActive','createdDate','UpdatedDate']
df_prod= pd.read_csv(r'C:\Users\Admin\Downloads\Data thecnogeeks\Data_Engineering\PythonProject\CSV_s1\products.csv',header=None,names=products_column)
print(df_prod.head())
transactions_column = ['txnno','txndate','custno','amount','productno','spendby']
df_tran=pd.read_csv(r'C:\Users\Admin\Downloads\Data thecnogeeks\Data_Engineering\PythonProject\CSV_s1\transactions.csv',header=None,names=transactions_column)
print(df_tran.head())

print('Usecase-2 Display only those customer fromn Csv1_s1 Who Purchased more than 3 product')
#df=df_tran['custno'].value_counts()
print(df_tran['custno'].value_counts()[df_tran['custno'].value_counts()>3])
#crossed Verified
print(df_tran[df_tran['custno']==391])

print('Usecase-3 Display Top 5 most Demanded Products')
#df=df_tran['productno'].value_counts().head()
print(df_tran['productno'].value_counts().head())
#crossed Verified
print(df_tran[df_tran['productno']==82])

print('Usecase-4 Display Top most trasaction Amount from Csv_s1')
print(df_tran.sort_values(by='amount',ascending=False).head())
#crossed Verified
print(df_tran['amount'].max())

print('Usecase-5 Diaplay Distinct Proffession from Csv_s1')
print(df_cust['profession'].unique())

print('Usecase-5 Display highest age in Csv_s1 Custmers Dataset')
print(df_cust['age'].max())

print('Usecase-7 Display custno, gender, age, profession, contactno, productno, productName,txndate, spendby, amount from CSV_s1 for custno = 923')
a=pd.merge(df_tran,df_prod,on='productno',how='inner')
df_tran_prod_cust = pd.merge(a,df_cust,on='custno',how='inner')
print(df_tran_prod_cust[df_tran_prod_cust['custno']==923][['custno','gender','age','profession','contactNo','productno','productName','txndate','spendby','amount']])

print('Usecase-8 Display All three PSV in pandas DataFrame and Display First Five Record')
customers_column = ['custno','firstname','lastname','gender','age','profession','contactNo','emailId','city','state','isActive ','createdDate','UpdatedDate']
df_psv_cust=pd.read_csv(r'C:\Users\Admin\Downloads\Data thecnogeeks\Data_Engineering\PythonProject\PSV_s2\customers.txt',sep='|',names=customers_column)
print(df_psv_cust.head())
df_psv_prod=pd.read_csv(r'C:\Users\Admin\Downloads\Data thecnogeeks\Data_Engineering\PythonProject\PSV_s2\products.txt',sep='|',names=products_column)
print(df_psv_prod.head())
df_psv_tran=pd.read_csv(r'C:\Users\Admin\Downloads\Data thecnogeeks\Data_Engineering\PythonProject\PSV_s2\transactions.txt',sep='|',names=transactions_column)
print(df_psv_tran.head())

print('Usecase-9 Display All three JSON in pandas DataFrame and Display First Five Record')
df_json_cust=pd.read_json(r'C:\Users\Admin\Downloads\Data thecnogeeks\Data_Engineering\PythonProject\JSON_s3\customers.json',lines=True)
print(df_json_cust.head())
df_json_prod=pd.read_json(r'C:\Users\Admin\Downloads\Data thecnogeeks\Data_Engineering\PythonProject\JSON_s3\products.json',lines=True)
print(df_json_prod.head())
df_json_cust=pd.read_json(r'C:\Users\Admin\Downloads\Data thecnogeeks\Data_Engineering\PythonProject\JSON_s3\transactions.json',lines=True)
print(df_json_cust.head())

print('Usecase-10 Display All three XML in pandas DataFrame and Display First Five Record')
df_xml_cust=pd.read_xml(r'C:\Users\Admin\Downloads\Data thecnogeeks\Data_Engineering\PythonProject\XML_s4\customers.xml')
print(df_xml_cust.head())
df_xml_tran=pd.read_xml(r'C:\Users\Admin\Downloads\Data thecnogeeks\Data_Engineering\PythonProject\XML_s4\transactions.xml')
print(df_xml_tran.head())
df_xml_prod=pd.read_xml(r'C:\Users\Admin\Downloads\Data thecnogeeks\Data_Engineering\PythonProject\XML_s4\products.xml')
print(df_xml_prod.head())


