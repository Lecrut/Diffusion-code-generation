import datetime

def compute_seconds_remaining_in_month():
    now = datetime.datetime.now()
    if now.month == 12:
        next_month = datetime.datetime(now.year + 1, 1, 1)
    else:
        next_month = datetime.datetime(now.year, now.month + 1, 1)
    last_day_of_month = next_month - datetime.timedelta(days=1)
    end_of_month = datetime.datetime(now.year, last_day_of_month.month, last_day_of_month.day, 23, 59, 59)
    delta = end_of_month - now
    total_seconds = int(delta.total_seconds())
    return total_seconds

if __name__ == '__main__':
    result = compute_seconds_remaining_in_month()
    print(result)