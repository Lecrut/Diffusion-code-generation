import time

def get_elapsed_seconds_today() -> int:
    units = {
        'hours': 3600,
        'minutes': 60,
        'seconds': 1
    }
    current_time = time.localtime()
    total_seconds = 0
    for unit_name, multiplier in units.items():
        if unit_name == 'hours':
            value = current_time.tm_hour
        elif unit_name == 'minutes':
            value = current_time.tm_min
        else:
            value = current_time.tm_sec
        total_seconds += value * multiplier
    return total_seconds

if __name__ == '__main__':
    elapsed = get_elapsed_seconds_today()
    print(elapsed)