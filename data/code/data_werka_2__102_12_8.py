import datetime

def is_weekday(date_value):
    if not isinstance(date_value, datetime.date):
        raise ValueError("Input must be a datetime.date object")
    return date_value.weekday() < 5

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 23)
    result = is_weekday(sample_date)
    print(result)