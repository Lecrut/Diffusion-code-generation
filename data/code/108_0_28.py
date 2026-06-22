import datetime

def get_day_of_month(date_obj):
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Input must be a datetime.date object")
    return date_obj.day

if __name__ == '__main__':
    target_date = datetime.date(1999, 12, 31)
    day_value = get_day_of_month(target_date)
    print(day_value)