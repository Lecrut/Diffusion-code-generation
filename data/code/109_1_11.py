import datetime

def seconds_left_in_month(timestamp: float) -> int:
    dt = datetime.datetime.fromtimestamp(timestamp)
    if dt.month == 12:
        next_month = datetime.datetime(dt.year + 1, 1, 1)
    else:
        next_month = datetime.datetime(dt.year, dt.month + 1, 1)
    start_of_current_month = datetime.datetime(dt.year, dt.month, 1)
    total_seconds_in_month = (next_month - start_of_current_month).total_seconds()
    elapsed_seconds = (dt - start_of_current_month).total_seconds()
    remaining_seconds = total_seconds_in_month - elapsed_seconds
    return int(remaining_seconds)

if __name__ == '__main__':
    now = datetime.datetime.now().timestamp()
    result = seconds_left_in_month(now)
    print(result)