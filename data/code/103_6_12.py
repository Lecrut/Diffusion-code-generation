import time

def seconds_elapsed_today():
    current_time = time.time()
    midnight = time.mktime((time.localtime(current_time).tm_year, 
                             time.localtime(current_time).tm_mon, 
                             time.localtime(current_time).tm_mday, 0, 0, 0, 
                             0, 0, -1))
    return int(current_time - midnight)

if __name__ == '__main__':
    sample_midnight = time.mktime((2023, 10, 27, 0, 0, 0, 0, 0, -1))
    elapsed_seconds = seconds_elapsed_today()
    print(elapsed_seconds)