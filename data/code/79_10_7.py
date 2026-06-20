import datetime

def is_valid_datetime(date_obj):
    return isinstance(date_obj, datetime.datetime)

def get_next_month_date(date):
    if not is_valid_datetime(date):
        raise ValueError("Input must be a datetime object")
    
    year = date.year
    month = date.month + 1
    
    if month > 12:
        month = 1
        year += 1
    
    return datetime.datetime(year, month, 1)

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 4, 15)
    next_month_date = get_next_month_date(sample_date)
    print(next_month_date.strftime("%Y-%m-%d"))