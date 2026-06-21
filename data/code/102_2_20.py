import datetime

WEEKEND_THRESHOLD = 5

def is_weekday(date_obj):
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Input must be a datetime.date object")
    return date_obj.weekday() < WEEKEND_THRESHOLD

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 25)
    result = is_weekday(sample_date)
    print(result)