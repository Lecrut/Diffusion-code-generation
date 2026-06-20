import datetime

def get_first_day_of_next_month(date_obj):
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Input must be a datetime.date object")
    
    next_month = date_obj.replace(day=1) + datetime.timedelta(days=32)
    return next_month.replace(day=1)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    first_day_next_month = get_first_day_of_next_month(sample_date)
    print(f"Original Date: {sample_date}")
    print(f"First Day of Next Month: {first_day_next_month}")
    
    sample_date_dec = datetime.date(2023, 12, 31)
    first_day_next_month_dec = get_first_day_of_next_month(sample_date_dec)
    print(f"Original Date: {sample_date_dec}")
    print(f"First Day of Next Month: {first_day_next_month_dec}")