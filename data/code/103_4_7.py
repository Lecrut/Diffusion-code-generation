from datetime import datetime

def fractional_day_to_seconds():
    now = datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    fractional_day = (now - start_of_day).total_seconds() / 86400
    return fractional_day * 86400

if __name__ == '__main__':
    print(fractional_day_to_seconds())