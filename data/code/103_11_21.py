import time

def get_seconds_since_midnight() -> float:
    current_time = time.time()
    seconds_in_day = 86400
    seconds_since_midnight = current_time % seconds_in_day
    return seconds_since_midnight

if __name__ == '__main__':
    result = get_seconds_since_midnight()
    print(result)