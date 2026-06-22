import datetime
import calendar

SECONDS_PER_MINUTE = 60

def calculate_remaining_minutes_in_month():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    _, days_in_month = calendar.monthrange(year, month)
    current_day = now.day
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second
    remaining_days = days_in_month - current_day
    remaining_hours = 23 - current_hour
    remaining_minutes = 59 - current_minute
    total_remaining_seconds = (remaining_days * 24 * SECONDS_PER_MINUTE) + (remaining_hours * SECONDS_PER_MINUTE) + remaining_minutes
    if current_second > 0:
        total_remaining_seconds += 1
    return total_remaining_seconds // SECONDS_PER_MINUTE

if __name__ == '__main__':
    result = calculate_remaining_minutes_in_month()
    print(result)