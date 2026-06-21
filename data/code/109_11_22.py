import datetime
import calendar

def time_remaining_in_month(year, month):
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second

    if year < current_year or (year == current_year and month < current_month):
        raise ValueError("The specified month and year are in the past.")

    if year == current_year and month == current_month:
        days_in_month = calendar.monthrange(year, month)[1]
        end_of_month = datetime.datetime(year, month, days_in_month, 23, 59, 59)
        current_time = now.replace(microsecond=0)
        delta = end_of_month - current_time
        total_seconds = int(delta.total_seconds())
    else:
        days_in_month = calendar.monthrange(year, month)[1]
        start_of_month = datetime.datetime(year, month, 1, 0, 0, 0)
        end_of_month = datetime.datetime(year, month, days_in_month, 23, 59, 59)
        current_time = now.replace(microsecond=0)
        delta = end_of_month - current_time
        total_seconds = int(delta.total_seconds())

    if total_seconds < 0:
        total_seconds = 0

    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    return {
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    result = time_remaining_in_month(2024, 12)
    print(result)