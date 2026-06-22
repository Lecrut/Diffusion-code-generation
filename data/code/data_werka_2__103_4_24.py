import datetime
import calendar

def calculate_seconds_passed_in_day(year, month, day, hour, minute, second, microsecond=0):
    if not isinstance(year, int) or year < 1:
        raise ValueError("Year must be a positive integer")
    if not isinstance(month, int) or month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if not isinstance(day, int) or day < 1:
        raise ValueError("Day must be a positive integer")
    if not isinstance(hour, int) or hour < 0 or hour > 23:
        raise ValueError("Hour must be between 0 and 23")
    if not isinstance(minute, int) or minute < 0 or minute > 59:
        raise ValueError("Minute must be between 0 and 59")
    if not isinstance(second, int) or second < 0 or second > 59:
        raise ValueError("Second must be between 0 and 59")
    if not isinstance(microsecond, int) or microsecond < 0 or microsecond > 999999:
        raise ValueError("Microsecond must be between 0 and 999999")
    
    days_in_month = calendar.monthrange(year, month)[1]
    if day > days_in_month:
        raise ValueError(f"Day {day} is invalid for month {month} in year {year}")

    try:
        target_dt = datetime.datetime(year, month, day, hour, minute, second, microsecond)
    except ValueError as e:
        raise ValueError(f"Invalid datetime components: {e}")

    start_of_day_dt = datetime.datetime(year, month, day)
    delta = target_dt - start_of_day_dt
    return delta.total_seconds()

if __name__ == '__main__':
    result = calculate_seconds_passed_in_day(2023, 10, 5, 12, 30, 45, 123456)
    print(result)