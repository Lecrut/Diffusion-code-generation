def get_day_from_epoch(epoch):
    seconds_in_day = 86400
    days_since_epoch = epoch // seconds_in_day
    current_day_of_month = 1
    current_month = 1
    current_year = 1970
    remaining_days = days_since_epoch
    while True:
        days_in_current_year = 366 if (current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)) else 365
        if remaining_days < days_in_current_year:
            break
        remaining_days -= days_in_current_year
        current_year += 1
    while True:
        if current_month in (1, 3, 5, 7, 8, 10, 12):
            days_in_month = 31
        elif current_month in (4, 6, 9, 11):
            days_in_month = 30
        elif current_month == 2:
            days_in_month = 29 if (current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)) else 28
        if remaining_days < days_in_month:
            break
        remaining_days -= days_in_month
        current_month += 1
    current_day_of_month = remaining_days + 1
    return current_day_of_month

if __name__ == '__main__':
    sample_timestamps = [0, 86400, 1609459200, 1640995200]
    for ts in sample_timestamps:
        day = get_day_from_epoch(ts)
        print(day)