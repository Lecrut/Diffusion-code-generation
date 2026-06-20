import time

def calculate_elapsed_time_fraction():
    start_of_day = int(time.mktime((time.localtime().tm_year, 
                                   time.localtime().tm_mon, 
                                   time.localtime().tm_mday, 
                                   0, 0, 0, 0, 0, 0)))
    current_time = int(time.time())
    elapsed_seconds = current_time - start_of_day
    total_seconds_in_day = 24 * 3600
    return elapsed_seconds / total_seconds_in_day

if __name__ == '__main__':
    fraction = calculate_elapsed_time_fraction()
    print(fraction)