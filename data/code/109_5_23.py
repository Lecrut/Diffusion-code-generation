import datetime
import calendar

SECONDS_PER_MINUTE = 60
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60

def calculate_remaining_minutes_in_current_month():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    last_day = calendar.monthrange(year, month)[1]
    current_day = now.day
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second
    remaining_days = last_day - current_day
    remaining_hours_in_current_day = HOURS_PER_DAY - 1 - current_hour
    remaining_minutes_in_current_day = MINUTES_PER_HOUR - 1 - current_minute
    remaining_seconds_in_current_day = SECONDS_PER_MINUTE - current_second
    total_remaining_minutes = (remaining_days * HOURS_PER_DAY * MINUTES_PER_HOUR) + (remaining_hours_in_current_day * MINUTES_PER_HOUR) + remaining_minutes_in_current_day
    if remaining_seconds_in_current_day > 0:
        total_remaining_minutes += 1
    return total_remaining_minutes

if __name__ == '__main__':
    result = calculate_remaining_minutes_in_current_month()
    print(result)