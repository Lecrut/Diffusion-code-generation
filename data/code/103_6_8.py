import time

def seconds_elapsed_today():
    current_time = time.time()
    midnight = int(time.mktime((current_time.year, current_time.month, current_time.day, 0, 0, 0, 0, 0, -1)))
    return int(current_time - midnight)

if __name__ == '__main__':
    print(seconds_elapsed_today())