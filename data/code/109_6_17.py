from datetime import datetime, timedelta

def fraction_of_month_remaining(year: int, month: int, day: int, hour: int, minute: int, second: int) -> float:
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second

    if current_year < year or (current_year == year and current_month < month):
        return 1.0
    if current_year > year or (current_year == year and current_month > month):
        return 0.0

    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_month_map = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if not is_leap:
        days_in_month_map[2] = 28

    total_days_in_month = days_in_month_map[month]
    days_passed = current_day - day
    hours_passed = current_hour - hour
    minutes_passed = current_minute - minute
    seconds_passed = current_second - second

    total_seconds_in_month = total_days_in_month * 24 * 60 * 60
    elapsed_seconds = (days_passed * 24 * 60 * 60) + (hours_passed * 60 * 60) + (minutes_passed * 60) + seconds_passed

    if elapsed_seconds < 0:
        elapsed_seconds = 0
    if elapsed_seconds > total_seconds_in_month:
        elapsed_seconds = total_seconds_in_month

    return 1.0 - (elapsed_seconds / total_seconds_in_month)

if __name__ == '__main__':
    start_year = 2023
    start_month = 10
    start_day = 15
    start_hour = 10
    start_minute = 30
    start_second = 0
    result = fraction_of_month_remaining(start_year, start_month, start_day, start_hour, start_minute, start_second)
    print(result)