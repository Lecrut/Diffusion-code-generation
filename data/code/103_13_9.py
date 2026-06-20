import time

def fractional_day():
    current_time = time.localtime()
    elapsed_seconds = (current_time.tm_hour * 3600) + (current_time.tm_min * 60) + current_time.tm_sec
    total_seconds_in_a_day = 24 * 3600
    return elapsed_seconds / total_seconds_in_a_day

if __name__ == '__main__':
    print(fractional_day())