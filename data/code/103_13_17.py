import time

def get_fractional_day():
    now = time.localtime()
    seconds_in_day = 24 * 60 * 60
    elapsed_seconds = (now.tm_hour * 3600) + (now.tm_min * 60) + now.tm_sec
    return elapsed_seconds / seconds_in_day

if __name__ == '__main__':
    result = get_fractional_day()
    print(result)