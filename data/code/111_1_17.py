import datetime

def validate_date(date_obj):
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Input must be an instance of datetime.date")

def add_30_days(date_obj):
    validate_date(date_obj)
    new_date = date_obj + datetime.timedelta(days=30)
    return new_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    sample_date = datetime.date(2024, 7, 4)
    result = add_30_days(sample_date)
    print(f"Result: {result}")