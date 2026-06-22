import datetime

def extract_day_component(target_date):
    if not isinstance(target_date, datetime.date):
        raise ValueError("Expected a datetime.date instance")
    day_number = target_date.day
    return day_number

if __name__ == '__main__':
    fixed_date = datetime.date(2025, 2, 14)
    day_result = extract_day_component(fixed_date)
    print(day_result)