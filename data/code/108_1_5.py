def get_day_of_month(timestamp):
    if not isinstance(timestamp, (int, float)):
        raise ValueError('Timestamp must be a number')
    if timestamp < 0:
        raise ValueError('Timestamp must be non-negative')
    total_seconds = int(timestamp)
    total_days = total_seconds // 86400
    year = 1970
    remaining_days = total_days
    while True:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days_in_current_year = 366 if is_leap else 365
        if remaining_days < days_in_current_year:
            break
        remaining_days -= days_in_current_year
        year += 1
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap:
        month_days[1] = 29
    month = 0
    while remaining_days >= month_days[month]:
        remaining_days -= month_days[month]
        month += 1
    day = remaining_days + 1
    return day

if __name__ == '__main__':
    print(get_day_of_month(1672531200))
    print(get_day_of_month(0))
    print(get_day_of_month(1609459200))