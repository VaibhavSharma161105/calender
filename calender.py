import calendar
import datetime
import pandas as pd
remind=[]
todo=[]
# reminders=pd.DataFrame('remind':remind,'todo':todo)
def today():
    x=datetime.datetime.now()
    date=x.strftime("%d")
    month=x.strftime("%B")
    year=x.strftime("%Y")
    day=x.strftime("%a")
    print("date:",date)
    print("month:",month)
    print("year:",year)
    print("day:",day)
def mycalendar():
    type=input('do you want year calender(y) or month calender(m):')
    if type=='y':
        yy=int(input("enter year:"))
        print(calendar.calendar(yy))
    if type=='m':
        yy=int(input("enter year:"))
        mm=int(input("enter month:"))
        print(calendar.month(yy, mm))
def setreminder():
    dd=int(input("enter date:"))
    mm=int(input("enter month:"))
    yy=int(input("enter year:"))
    ss=input("enter title:")
    date=f'{yy}/{mm}/{dd}'
    #
    # date should be iin correct format
    #
    if dd<10:
        date=f'{yy}/{mm}/0{dd}'
    if mm<10:
        date=f'{yy}/0{mm}/{dd}'
#
# while adding new data previous should not be deleted
#
    reminders = pd.read_csv('data.csv')  
    remind=list(reminders["remind on"])
    todo=list(reminders["to do"])
    remind.append(date)
    todo.append(ss)
    df={"remind on":remind,"to do":todo}
    reminders=pd.DataFrame(df)
    reminders.to_csv('data.csv', index=False)
    print(f"Reminder set for: {date}")
    print(reminders)
def viewreminders():
    reminders = pd.read_csv('data.csv')  
    print(reminders)
#
# check this function again
#
def remindme():
    reminders = pd.read_csv('data.csv')  
    x = datetime.datetime.now()
    today = x.strftime("%Y/%m/%d")
    
    today_reminders = reminders[reminders['remind on'] == today]

    if not today_reminders.empty:
        print("Reminders for today:")
        for i, row in today_reminders.iterrows():
            print(f"Reminder: {row['remind on']}, Task: {row['to do']}")
    else:
        print("No reminders for today.")

def reminderover():
    reminders = pd.read_csv('data.csv')  
    x = datetime.datetime.now()
    today = x.strftime("%Y/%m/%d")
    reminders = reminders[reminders['remind on'] > today]
    # reminders=pd.DataFrame(reminders)not this but
    reminders.to_csv('data.csv', index=False)

    
    
print("welcome to mycalender")
today()
remindme()
reminderover()
#
n=100
while n !=0:
    print("press 1 for calendar")
    print("press 2 to set reminder")
    print("press 3 to view reminders")
    n=int(input("enter your response:"))
    if n==1:
        mycalendar()
    elif n==2:
        setreminder()
    elif n==3:
        viewreminders()
    else:
        print("please enter a valid respoonse")       


    
