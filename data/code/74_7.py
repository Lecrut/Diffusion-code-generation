import datetime
from functools import wraps
def prepend_day_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'date' in kwargs:
            date_obj = kwargs.pop('date')
            day_name = date_obj.strftime('%A')
            new_date = datetime.datetime(date_obj.year, date_obj.month, date_obj.day, 0, 0, 0)
            new_date.replace(day=date_obj.day, month=date_obj.month, year=date_obj.year)
            return {**kwargs, 'date': new_date, 'day_name': day_name}
        elif args and isinstance(args[0], datetime.date):
            date_obj = args[0]
            day_name = date_obj.strftime('%A')
            new_date = datetime.datetime(date_obj.year, date_obj.month, date_obj.day)
            return (day_name, new_date)
        else:
            return func(*args, **kwargs)
    return wrapper
@prepend_day_name
def format_date_with_name(date_obj):
    return date_obj
if __name__ == '__main__':
    sample_date_1 = datetime.date(2023, 10, 26)
    sample_date_2 = datetime.datetime(2024, 1, 1)
    result_1 = format_date_with_name(sample_date_1)
    print(f"Input Date 1: {sample_date_1}")
    print(f"Result 1: {result_1}")
    result_2 = format_date_with_name(sample_date_2)
    print(f"Input Date 2: {sample_date_2}")
    print(f"Result 2: {result_2}")