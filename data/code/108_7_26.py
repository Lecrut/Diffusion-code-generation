def get_day_from_epoch(timestamp):
    if not isinstance(timestamp, (int, float)):
        raise ValueError("Timestamp must be an integer or float")
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    seconds_in_day = 86400
    days_since_epoch = int(timestamp // seconds_in_day)
    total_days = days_since_epoch + 1
    year = 1970
    while True:
        days_in_year = 366 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 365
        if total_days <= days_in_year:
            break
        total_days -= days_in_year
        year += 1
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        month_days[2] = 29
    month = 1
    while total_days > month_days[month]:
        total_days -= month_days[month]
        month += 1
    return total_days

if __name__ == '__main__':
    epoch_timestamp = 1609459200
    day = get_day_from_epoch(epoch_timestamp)
    print(day)