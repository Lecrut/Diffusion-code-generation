import time

def calculate_day_fraction():
    now = time.localtime()
    total_seconds_in_day = 86400
    current_seconds = (now.tm_hour * 3600) + (now.tm_min * 60) + now.tm_sec
    if total_seconds_in_day <= 0:
        raise ValueError("Total seconds in a day cannot be zero or negative")
    return current_seconds / total_seconds_in_day

if __name__ == '__main__':
    result = calculate_day_fraction()
    print(result)