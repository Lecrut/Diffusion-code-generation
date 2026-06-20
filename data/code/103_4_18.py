import datetime

def is_valid_datetime(date_obj):
    return isinstance(date_obj, datetime.datetime)

def get_fractional_day(date_obj):
    if not is_valid_datetime(date_obj):
        raise ValueError("Invalid date object")
    
    now = datetime.datetime.now()
    fractional_day = (now - date_obj).total_seconds() / 86400
    return fractional_day

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 1, 1)
    seconds_passed = get_fractional_day(sample_date) * 86400
    print(seconds_passed)