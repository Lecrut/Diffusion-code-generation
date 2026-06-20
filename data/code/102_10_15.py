import datetime

def is_valid_datetime(date_obj):
    if not isinstance(date_obj, datetime.datetime):
        return False
    return True

def is_weekday(dt):
    if not is_valid_datetime(dt):
        raise ValueError('Input must be a datetime object.')
    return dt.weekday() < 5
if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 5)
    print(is_weekday(sample_dt))