import time

def get_weekday_for_date(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    try:
        struct_time = time.strptime(date_str, "%Y-%m-%d")
        timestamp = time.mktime(struct_time)
        tm_wday = time.localtime(timestamp).tm_wday
        names = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        return names[tm_wday]
    except Exception as e:
        raise ValueError(f"Invalid date format: {date_str}") from e

if __name__ == '__main__':
    sample_date = '2023-01-01'
    weekday_name = get_weekday_for_date(sample_date)
    print(weekday_name)