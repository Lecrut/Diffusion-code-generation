import time

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def get_elapsed_seconds_today() -> int:
    current_time = time.localtime()
    hour_component = current_time.tm_hour
    minute_component = current_time.tm_min
    second_component = current_time.tm_sec
    total_seconds = (hour_component * SECONDS_PER_HOUR) + (minute_component * SECONDS_PER_MINUTE) + second_component
    return total_seconds

if __name__ == '__main__':
    result = get_elapsed_seconds_today()
    print(result)