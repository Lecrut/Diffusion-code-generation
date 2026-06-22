from datetime import datetime

def fraction_of_month_remaining(year: int, month: int, day: int, hour: int, minute: int, second: int) -> float:
    now = datetime.now()
    current_day = now.day
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second

    if now.year < year or (now.year == year and now.month < month):
        return 1.0
    if now.year > year or (now.year == year and now.month > month):
        return 0.0

    days_in_month_map = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if not is_leap:
        days_in_month_map[2] = 28

    total_days = days_in_month_map[month]
    days_remaining = total_days - current_day
    seconds_remaining_in_day = (23 - current_hour) * 3600 + (59 - current_minute) * 60 + (59 - current_second)
    
    if current_day == day and current_hour == hour and current_minute == minute and current_second == second:
        return 0.0

    total_seconds_in_period = total_days * 86400
    remaining_seconds = days_remaining * 86400 + seconds_remaining_in_day

    return remaining_seconds / total_seconds_in_period

if __name__ == '__main__':
    result = fraction_of_month_remaining(2023, 10, 1, 0, 0, 0)
    print(result)