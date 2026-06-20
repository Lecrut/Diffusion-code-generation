import time

SECONDS_PER_DAY = 24 * 60 * 60

def seconds_elapsed_today():
    current_time = time.time()
    midnight = time.mktime(time.localtime(current_time))
    return int(current_time - midnight)

if __name__ == '__main__':
    elapsed_seconds = seconds_elapsed_today()
    print(elapsed_seconds)