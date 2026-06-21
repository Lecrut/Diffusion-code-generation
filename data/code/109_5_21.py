import datetime

def remaining_minutes_in_current_month():
    now = datetime.datetime.now()
    first_day_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    if now.month == 12:
        next_month = now.replace(year=now.year + 1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    else:
        next_month = now.replace(month=now.month + 1, day=1, hour=0, minute=0, second=0, microsecond=0)
    total_seconds = (next_month - first_day_of_month).total_seconds()
    remaining_seconds = (next_month - now).total_seconds()
    remaining_minutes = remaining_seconds / 60
    return remaining_minutes

if __name__ == '__main__':
    result = remaining_minutes_in_current_month()
    print(result)