import time

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

def calculate_milliseconds_today():
    current_time = time.localtime()
    start_of_day = (current_time.tm_year, current_time.tm_mon, current_time.tm_mday, 0, 0, 0)
    seconds_since_midnight = int(time.mktime(start_of_day) - time.mktime((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, 0, 0, 0)))
    milliseconds = seconds_since_midnight * SECONDS_PER_MINUTE * MINUTES_PER_HOUR
    return milliseconds

if __name__ == '__main__':
    milliseconds = calculate_milliseconds_today()
    print(milliseconds)