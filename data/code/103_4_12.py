import datetime

def calculate_fractional_day_as_seconds():
    now = datetime.datetime.now()
    start_of_day = datetime.datetime(now.year, now.month, now.day)
    fractional_day = (now - start_of_day).total_seconds()
    return fractional_day

if __name__ == '__main__':
    elapsed_seconds = calculate_fractional_day_as_seconds()
    print(elapsed_seconds)