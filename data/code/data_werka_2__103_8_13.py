import time

def get_elapsed_seconds_today() -> int:
    current = time.localtime()
    hour_component = current.tm_hour
    minute_component = current.tm_min
    second_component = current.tm_sec
    hours_as_seconds = hour_component * 3600
    minutes_as_seconds = minute_component * 60
    total_elapsed = hours_as_seconds + minutes_as_seconds + second_component
    return total_elapsed

if __name__ == '__main__':
    sample_time_struct = time.struct_time((2023, 1, 1, 12, 30, 45, 0, 1, 0))
    simulated_seconds = (sample_time_struct.tm_hour * 3600) + (sample_time_struct.tm_min * 60) + sample_time_struct.tm_sec
    actual_seconds = get_elapsed_seconds_today()
    print(simulated_seconds)
    print(actual_seconds)