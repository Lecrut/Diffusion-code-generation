import datetime

DAYS_IN_WEEK = 7

def get_day_of_month(target_date):
    if not isinstance(target_date, datetime.date):
        raise ValueError("Input must be a datetime.date object")
    return target_date.day

def format_date_info(date_obj):
    day = date_obj.day
    weekday = date_obj.strftime("%A")
    return f"Day: {day}, Weekday: {weekday}"

if __name__ == '__main__':
    sample_date = datetime.date(2025, 5, 12)
    day_value = get_day_of_month(sample_date)
    info_string = format_date_info(sample_date)
    print(day_value)
    print(info_string)