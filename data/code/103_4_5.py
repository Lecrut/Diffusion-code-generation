from datetime import datetime

def fractional_day_to_seconds():
    now = datetime.now()
    start_of_day = datetime(now.year, now.month, now.day)
    fractional_day = (now - start_of_day).total_seconds() / 86400
    return fractional_day * 86400

if __name__ == '__main__':
    print(fractional_day_to_seconds())