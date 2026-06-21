import time

def get_fractional_day():
    current_time = time.localtime()
    seconds_in_day = 24 * 60 * 60
    seconds_elapsed = (current_time.tm_hour * 3600) + (current_time.tm_min * 60) + current_time.tm_sec
    return seconds_elapsed / seconds_in_day

if __name__ == '__main__':
    result = get_fractional_day()
    print(result)