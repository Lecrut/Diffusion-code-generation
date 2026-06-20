import time

def fractional_day():
    current_time = time.time()
    start_of_day = time.mktime(time.localtime(current_time))
    elapsed_seconds = current_time - start_of_day
    total_seconds_in_day = 24 * 60 * 60
    return elapsed_seconds / total_seconds_in_day

if __name__ == '__main__':
    print(fractional_day())