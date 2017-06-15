
# coding: utf-8

# In[ ]:

import csv
import argparse 
import datetime
    
    
FIELDS = ['id',"title", "location", "day", "start", "end"]

    # add event functionality
def add_event(ID,title,location,day,start,end):
   
    event = {'id':ID, 'title':title,'location':location,'day':day,'start':start,'end':end}
 
    with open('calendar.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS) 
        writer.writerow(event) 

    #Date & Time parsing: string to date format, event 4 and future input
    def strdate(dt):
        return dt.strftime("%Y-%d-%m")

    def strtime(tm):
        return dt.strftime("%H:%M")    
    
    # view functionality 
def view(args):
    
    with open('calendar.csv', 'r') as f:
            reader = csv.DictReader(f, fieldnames=FIELDS)
            event = [row for row in reader if row['id'] == ID]
            
        def strpdate(dt):    
            return dt.strpdate("%Y-%d-%m")
        
        def strptime(tm):
            return time.strptime("%H:%M")
            
            for row in event:
            print(row)
    
    # agenda functionality
def agenda(args):
     
    with open('calendar.csv', 'r') as f:
                reader = csv.DictReader(f, fieldnames=FIELDS)
                event = [row for row in reader if row['day'] == day]            

            def strpdate(dt):    
                return dt.strpdate("%Y-%d-%m")

            def strptime(tm):
                return time.strptime("%H:%M")

                for row in event:
                print (row)

    #week functionality            
def week(args):
current_day = date.today()
next_week = datetime.timedelta(days = 7)

[str(end_date + timedelta(days=x)) for x in range((start_date-end_date).days + 1)]

    def week(next_week):
    with open('calendar.csv', 'r') as f:
              reader = csv.DictReader(f, fieldnames=FIELDS)
              event = [row for row in reader if row['day'] in range(current_day, next_week)]          
            
            
            def strpdate(dt):    
                return dt.strpdate("%Y-%d-%m")

            def strptime(tm):
                return time.strptime("%H:%M")  
            
            for row in event:
            print (row)


if __name__ == "__main__": 

    parser = argparse.ArgumentParser(description="simple calendar management utility") 
    subparsers = parser.add_subparsers(help="calendar commands") 


    # Add event parser 
add_event_parser = subparsers.add_parser('add', help='add an event to the calendar') 
add_event_parser.set_defaults(func=add_event)
add event_parser.add_argument('--FIELDS', type=ls) 

# View parser 
view_parser = subparsers.add_parser('view', help='view event details') 
view_parser.set_defaults(func=view)
add view_parser.add_argument('view', type=values)

    # Agenda parser 
agenda_parser = subparsers.add_parser('agenda', help='print out the agenda for today') 
agenda_parser.set_defaults(func=agenda)
add agenda_parser.add_argument('agenda', type=values)

    # Week parser 
week_parser = subparsers.add_parser('week', help='display events this week') 
week_parser.set_defaults(func=week)
add week_parser.add_argument('week', type=values)

    # Parse args and execute correct function. 
args = parser.parse_args()
args.func(args)

