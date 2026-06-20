import datetime

def fractional_day_to_seconds(fractional_day):
    return fractional_day * 24 * 60 * 60

if __name__ == '__main__':
    now = datetime.datetime.now()
    start_of_day = datetime.datetime(now.year, now.month, now.day)
    fractional_day_passed = (now - start_of_day).total_seconds() / (24 * 60 * 60)
    seconds_passed_today = fractional_day_to_seconds(fractional_day_passed)
    print(seconds_passed_today)