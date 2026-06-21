import datetime

def seconds_remaining_in_current_month():
    now = datetime.datetime.now()
    last_day = now.replace(day=1) + datetime.timedelta(days=32)
    last_day = last_day.replace(day=1) - datetime.timedelta(days=1)
    last_second = last_day.replace(hour=23, minute=59, second=59)
    delta = last_second - now
    return int(delta.total_seconds())

if __name__ == '__main__':
    result = seconds_remaining_in_current_month()
    print(result)