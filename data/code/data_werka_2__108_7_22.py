def get_day_from_epoch(timestamp):
    if not isinstance(timestamp, int):
        raise ValueError("Timestamp must be an integer")
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    seconds_per_day = 86400
    total_days = timestamp // seconds_per_day
    current_year = 1970
    while True:
        is_leap = (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0)
        days_in_current_year = 366 if is_leap else 365
        if total_days < days_in_current_year:
            break
        total_days -= days_in_current_year
        current_year += 1
    months_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        months_days = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    month = 0
    while month < 12:
        if total_days < months_days[month]:
            break
        total_days -= months_days[month]
        month += 1
    day = total_days + 1
    return day

if __name__ == '__main__':
    sample_timestamp = 1609459200
    result = get_day_from_epoch(sample_timestamp)
    print(result)