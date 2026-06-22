import time

def get_weekday_from_date(date_string):
    if not isinstance(date_string, str):
        raise ValueError("date_string must be a string")
    if len(date_string) != 10:
        raise ValueError("date_string must be in YYYY-MM-DD format")
    try:
        parsed = time.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date provided")
    timestamp = time.mktime(parsed)
    local_time = time.localtime(timestamp)
    weekday_index = local_time.tm_wday
    weekday_names = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    return weekday_names[weekday_index]

if __name__ == '__main__':
    target_date = '2023-01-01'
    weekday = get_weekday_from_date(target_date)
    print(weekday)