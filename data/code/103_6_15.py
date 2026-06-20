import time

SECONDS_PER_DAY = 86400

def seconds_elapsed_today():
    now = time.time()
    midnight = time.mktime(time.localtime(now))
    return int(now - midnight)

if __name__ == '__main__':
    elapsed_seconds = seconds_elapsed_today()
    print(elapsed_seconds)