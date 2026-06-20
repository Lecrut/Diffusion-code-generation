from datetime import datetime, timedelta

def fractional_day_to_seconds():
    now = datetime.now()
    start_of_day = datetime(now.year, now.month, now.day)
    fractional_day = (now - start_of_day) / timedelta(days=1)
    seconds = fractional_day.total_seconds()
    return seconds

if __name__ == '__main__':
    print(fractional_day_to_seconds())