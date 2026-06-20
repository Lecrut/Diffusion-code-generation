import time

def seconds_elapsed_today():
    now = time.time()
    midnight = int(time.mktime((time.localtime(now).tm_year, time.localtime(now).tm_mon, time.localtime(now).tm_mday, 0, 0, 0, 0, 0, 0)))
    return int(now - midnight)

if __name__ == '__main__':
    print(seconds_elapsed_today())