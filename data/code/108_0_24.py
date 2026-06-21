import datetime

def get_day_component(date_instance):
    if not isinstance(date_instance, datetime.date):
        raise ValueError("Input must be a datetime.date object")
    day_value = date_instance.day
    return day_value

if __name__ == '__main__':
    target_date = datetime.date(1999, 12, 31)
    day_of_month = get_day_component(target_date)
    print(day_of_month)