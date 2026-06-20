import time

def fractional_day():
    now = time.localtime()
    elapsed_seconds = (now.tm_hour * 3600) + (now.tm_min * 60) + now.tm_sec
    total_seconds_in_day = 24 * 3600
    return elapsed_seconds / total_seconds_in_day

if __name__ == '__main__':
    print(fractional_day())