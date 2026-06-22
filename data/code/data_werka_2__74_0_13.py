import datetime
import calendar

def get_day_name(date_obj=None):
    if date_obj is None:
        date_obj = datetime.date.today()
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Expected a date object")
    return calendar.day_name[date_obj.weekday()]

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 25)
    current_date = datetime.date.today()
    
    print(get_day_name(sample_date))
    print(get_day_name(current_date))