import datetime

def compute_seconds_remaining_in_month():
    now = datetime.datetime.now()
    if now.month == 12:
        next_month = now.replace(year=now.year + 1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    else:
        next_month = now.replace(month=now.month + 1, day=1, hour=0, minute=0, second=0, microsecond=0)
    delta = next_month - now
    return int(delta.total_seconds())

if __name__ == '__main__':
    result = compute_seconds_remaining_in_month()
    print(result)