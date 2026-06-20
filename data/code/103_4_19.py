import datetime

def fractional_day_to_seconds(fractional_day):
    day_in_seconds = 24 * 60 * 60
    return fractional_day * day_in_seconds

if __name__ == '__main__':
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    fractional_day_passed = (now - start_of_day) / datetime.timedelta(days=1)
    seconds_passed = fractional_day_to_seconds(fractional_day_passed)
    print(seconds_passed)