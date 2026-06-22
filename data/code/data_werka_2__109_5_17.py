import datetime

def get_remaining_minutes_in_month():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    if month == 12:
        next_month = datetime.datetime(year + 1, 1, 1)
    else:
        next_month = datetime.datetime(year, month + 1, 1)
    last_day = next_month - datetime.timedelta(days=1)
    last_day = last_day.replace(hour=23, minute=59, second=59, microsecond=0)
    end_of_month = datetime.datetime(year, month, last_day.day, 23, 59, 59)
    remaining_seconds = (end_of_month - now).total_seconds()
    if remaining_seconds < 0:
        return 0
    return int(remaining_seconds / 60)

if __name__ == '__main__':
    result = get_remaining_minutes_in_month()
    print(result)