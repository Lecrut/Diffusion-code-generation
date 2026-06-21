import time

def compute_day_fraction():
    now = time.localtime()
    hours = now.tm_hour
    minutes = now.tm_min
    seconds = now.tm_sec
    if hours > 23 or minutes > 59 or seconds > 59:
        return 0.0
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds / 86400.0

if __name__ == '__main__':
    fraction = compute_day_fraction()
    print(fraction)