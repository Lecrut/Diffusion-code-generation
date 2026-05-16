import datetime
def is_weekday(date_tuple):
    date_obj = datetime.datetime.fromtimestamp(date_tuple)
    return date_obj.weekday() < 5
if __name__ == '__main__':
    date1 = 20231027          
    date2 = 20231028            
    date3 = 20231029          
    date4 = 20231030          
    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")
    print(f"Is {date3} a weekday? {is_weekday(date3)}")
    print(f"Is {date4} a weekday? {is_weekday(date4)}")