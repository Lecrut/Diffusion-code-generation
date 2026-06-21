def get_day_from_epoch(timestamp):
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    days_since_epoch = timestamp // 86400
    seconds_in_day = timestamp % 86400
    hours = seconds_in_day // 3600
    minutes = (seconds_in_day % 3600) // 60
    seconds = seconds_in_day % 60
    if hours != 0 or minutes != 0 or seconds != 0:
        days_since_epoch += 1
    year = 1970
    while True:
        days_in_year = 366 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 365
        if days_since_epoch < days_in_year:
            break
        days_since_epoch -= days_in_year
        year += 1
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        month_days[1] = 29
    month = 1
    while month_days[month - 1] <= days_since_epoch:
        days_since_epoch -= month_days[month - 1]
        month += 1
    day = days_since_epoch + 1
    return day

if __name__ == '__main__':
    print(get_day_from_epoch(0))
    print(get_day_from_epoch(86400))
    print(get_day_from_epoch(1609459200))
    print(get_day_from_epoch(1704067200))