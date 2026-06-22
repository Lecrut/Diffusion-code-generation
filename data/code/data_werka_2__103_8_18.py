import time

def get_elapsed_seconds_today() -> int:
    current = time.localtime()
    hour_value = current.tm_hour
    minute_value = current.tm_min
    second_value = current.tm_sec
    seconds_per_hour = 3600
    seconds_per_minute = 60
    total_elapsed = (hour_value * seconds_per_hour) + (minute_value * seconds_per_minute) + second_value
    return total_elapsed

if __name__ == '__main__':
    sample_result = get_elapsed_seconds_today()
    print(sample_result)