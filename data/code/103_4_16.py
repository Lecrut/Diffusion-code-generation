import datetime

def fractional_day_to_seconds():
    now = datetime.datetime.now()
    start_of_day = datetime.datetime(now.year, now.month, now.day)
    time_since_midnight = now - start_of_day
    fractional_day = time_since_midnight.total_seconds() / (24 * 3600)
    return fractional_day

if __name__ == '__main__':
    elapsed_seconds = fractional_day_to_seconds()
    print(elapsed_seconds)