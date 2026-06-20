import datetime

def fractional_day_to_seconds(fractional_day):
    return fractional_day * 24 * 60 * 60

if __name__ == '__main__':
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    fractional_day = (now - start_of_day).total_seconds() / (24 * 60 * 60)
    seconds_since_midnight = fractional_day_to_seconds(fractional_day)
    print(seconds_since_midnight)