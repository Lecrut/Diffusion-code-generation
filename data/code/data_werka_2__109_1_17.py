import datetime

def seconds_left_in_current_month(timestamp: float) -> int:
    dt = datetime.datetime.fromtimestamp(timestamp)
    if dt.month == 12:
        next_month = dt.replace(year=dt.year + 1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    else:
        next_month = dt.replace(month=dt.month + 1, day=1, hour=0, minute=0, second=0, microsecond=0)
    delta = next_month - dt
    return int(delta.total_seconds())

if __name__ == '__main__':
    now = datetime.datetime.now().timestamp()
    result = seconds_left_in_current_month(now)
    print(result)