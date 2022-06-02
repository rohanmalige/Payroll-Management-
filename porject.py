import mysql.connector
conobj=mysql.connector.connect(host="localhost",user="root",passwd="")
cur=conobj.cursor()
try:
    cur.execute("create database Payroll_Management_System")
except:
    print()
cur.execute("use Payroll_Management_System")
try:
    cur.execute("drop table Employee_Details")
except:
    print()
cur.execute("create table Employee_Details(E_no. varchar(5) primary key, E_name varchar(40), Gender char(1), DOB date(), DOJ date(),")
cur.execute("insert into records values('E001','Advaith','M','',')")
cur.execute("insert into records values('E002','Aamir','M','','')")
cur.execute("insert into records values('E003',')")
cur.execute("insert into records values('E004',')")
cur.execute("insert into records values('E005',')")
cur.execute("insert into records values('E006','")
cur.execute("insert into records values('E007','")
conobj.commit()
try:
  cur.execute("drop Salary_Details")
except:
  print()
cur.execute("create table Employee_Details(E_no. varchar(5) primary key, E_name varchar(40), Working_days INT(3), Basic INT(6), DOJ date(),")
cur.execute("insert into records values('E001','Advaith','M','',')")
cur.execute("insert into records values('E002','Aamir','M','','')")
cur.execute("insert into records values('E003',')")
cur.execute("insert into records values('E004',')")
cur.execute("insert into records values('E005',')")
cur.execute("insert into records values('E006','")
cur.execute("insert into records values('E007','")
conobj.commit()

def Menu():
    while cont=="Y" or cont=="y":
        print("1.Addition of records")
        print("2.Modification except employee number and employee name")
        print("3.Searching an employee by empno,empname")
        print("4.Input number of days worked and other deductions of each employee in monthly pay file")
        print("5.Reports")
        choice=input(int("enter your choice"))
        if choice==1:
            print("enter the details you want to add with quotes and commas")
            
        
        
        

