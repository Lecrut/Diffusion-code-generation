import time

def calculate_fractional_day_part():
    now = time.localtime()
    seconds_per_hour = 3600
    minutes_per_hour = 60
    seconds_per_day = 86400
    elapsed_seconds = (now.tm_hour * seconds_per_hour) + (now.tm_min * minutes_per_hour) + now.tm_sec
    fraction = elapsed_seconds / seconds_per_day
    return fraction

if __name__ == '__main__':
    result = calculate_fractional_day_part()
    print(result)