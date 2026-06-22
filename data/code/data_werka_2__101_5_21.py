import time

def get_weekday_for_date(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    if len(date_str) != 10:
        raise ValueError("Invalid date format")
    parts = date_str.split("-")
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    try:
        int(parts[0])
        int(parts[1])
        int(parts[2])
    except ValueError:
        raise ValueError("Invalid date format")
    struct_time = time.strptime(date_str, "%Y-%m-%d")
    timestamp = time.mktime(struct_time)
    local_time = time.localtime(timestamp)
    weekday_code = local_time.tm_wday
    names = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    return names[weekday_code]

if __name__ == '__main__':
    sample_date = '2023-01-01'
    weekday_name = get_weekday_for_date(sample_date)
    print(weekday_name)