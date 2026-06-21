import time
import calendar

def get_fractional_day_seconds():
    current_timestamp = time.time()
    seconds_today = current_timestamp % 86400
    return seconds_today

if __name__ == '__main__':
    result = get_fractional_day_seconds()
    print(result)