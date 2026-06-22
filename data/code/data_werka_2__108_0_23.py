import datetime

DAY_ATTRIBUTE = "day"

def retrieve_day_component(date_instance):
    if not isinstance(date_instance, datetime.date):
        raise ValueError("Input must be a datetime.date object")
    return date_instance.day

if __name__ == '__main__':
    fixed_date = datetime.date(1999, 12, 31)
    day_value = retrieve_day_component(fixed_date)
    print(day_value)