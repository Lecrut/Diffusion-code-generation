import calendar

def parse_timestamp_to_date(timestamp):
    if not isinstance(timestamp, int):
        raise ValueError("Timestamp must be an integer")
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    seconds_in_day = 86400
    epoch_year = 1970
    remaining_seconds = timestamp
    year = epoch_year
    while True:
        is_leap = calendar.isleap(year)
        days_in_current_year = 366 if is_leap else 365
        seconds_in_current_year = days_in_current_year * seconds_in_day
        if remaining_seconds < seconds_in_current_year:
            break
        remaining_seconds -= seconds_in_current_year
        year += 1
    days_in_current_year = 366 if calendar.isleap(year) else 365
    day_of_year = remaining_seconds // seconds_in_day
    month = 1
    while month <= 12:
        days_in_month = calendar.monthrange(year, month)[1]
        if day_of_year < days_in_month:
            break
        day_of_year -= days_in_month
        month += 1
    day = day_of_year + 1
    return f"{year:04d}/{month:02d}/{day:02d}"

if __name__ == '__main__':
    sample_timestamps = [0, 86400, 1609459200, 1640995200, 2147483647]
    for ts in sample_timestamps:
        result = parse_timestamp_to_date(ts)
        print(result)