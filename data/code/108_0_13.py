import datetime

def get_day_from_date(target_date):
    if not isinstance(target_date, datetime.date):
        raise ValueError("Input must be a datetime.date object")
    return target_date.day

if __name__ == '__main__':
    fixed_date = datetime.date(2024, 7, 4)
    day_value = get_day_from_date(fixed_date)
    print(day_value)