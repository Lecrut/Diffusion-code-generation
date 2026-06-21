import datetime

def compute_seconds_remaining_in_month():
    now = datetime.datetime.now()
    if now.month == 12:
        next_month = datetime.datetime(now.year + 1, 1, 1)
    else:
        next_month = datetime.datetime(now.year, now.month + 1, 1)
    last_second_of_month = next_month - datetime.timedelta(seconds=1)
    delta = last_second_of_month - now
    total_seconds = int(delta.total_seconds())
    return total_seconds

if __name__ == '__main__':
    result = compute_seconds_remaining_in_month()
    print(result)