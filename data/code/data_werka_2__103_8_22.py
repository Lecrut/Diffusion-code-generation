import time

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def get_elapsed_seconds_today() -> int:
    local_time = time.localtime()
    hour_component = local_time.tm_hour
    minute_component = local_time.tm_min
    second_component = local_time.tm_sec
    total_seconds = hour_component * SECONDS_PER_HOUR
    total_seconds += minute_component * SECONDS_PER_MINUTE
    total_seconds += second_component
    return total_seconds

if __name__ == '__main__':
    sample_time = time.localtime()
    computed_value = get_elapsed_seconds_today()
    print(computed_value)