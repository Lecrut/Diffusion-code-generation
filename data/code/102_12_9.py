import datetime

def is_weekday(date_value):
    if isinstance(date_value, datetime.date) and not isinstance(date_value, datetime.datetime):
        return date_value.weekday() < 5
    if isinstance(date_value, datetime.datetime):
        return date_value.weekday() < 5
    raise ValueError("Unsupported input type")

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 23)
    result = is_weekday(sample_date)
    print(result)