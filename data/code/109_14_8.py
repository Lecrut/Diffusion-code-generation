from datetime import datetime
from calendar import monthrange

def get_remaining_month_time(target_date: datetime):
    current_year = target_date.year
    current_month = target_date.month
    if current_month == 12:
        next_month_start_year = current_year + 1
        next_month_start_month = 1
    else:
        next_month_start_year = current_year
        next_month_start_month = current_month + 1
    next_month_start = datetime(next_month_start_year, next_month_start_month, 1)
    time_delta = next_month_start - target_date
    total_seconds = int(time_delta.total_seconds())
    if total_seconds < 0:
        total_seconds = 0
    days = total_seconds // 86400
    remainder_after_days = total_seconds % 86400
    hours = remainder_after_days // 3600
    remainder_after_hours = remainder_after_days % 3600
    minutes = remainder_after_hours // 60
    seconds = remainder_after_hours % 60
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15, 14, 30, 45)
    result = get_remaining_month_time(sample_date)
    print(result)