import datetime

def extract_day(date_instance):
    if not isinstance(date_instance, datetime.date):
        raise ValueError("Expected a datetime.date object")
    return date_instance.day

if __name__ == '__main__':
    fixed_date = datetime.date(2024, 1, 31)
    day_value = extract_day(fixed_date)
    print(day_value)