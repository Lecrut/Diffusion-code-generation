import datetime

def is_valid_date(date_obj):
    try:
        date_str = date_obj.strftime('%Y-%m-%d')
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def first_day_next_month(date_obj):
    if not is_valid_date(date_obj):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    next_month = date_obj.replace(day=28) + datetime.timedelta(days=4)
    return next_month.replace(day=1)

if __name__ == '__main__':
    sample_date = datetime.datetime(2024, 3, 31)
    print(first_day_next_month(sample_date).strftime('%Y-%m-%d'))