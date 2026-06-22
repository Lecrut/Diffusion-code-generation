import time

def calculate_day_fraction():
    now = time.localtime()
    current_hour = now.tm_hour
    current_minute = now.tm_min
    current_second = now.tm_sec
    seconds_per_hour = 3600
    seconds_per_minute = 60
    total_seconds_elapsed = (current_hour * seconds_per_hour) + (current_minute * seconds_per_minute) + current_second
    total_seconds_in_day = 86400
    fraction = total_seconds_elapsed / total_seconds_in_day
    return fraction

if __name__ == '__main__':
    sample_result = calculate_day_fraction()
    print(sample_result)