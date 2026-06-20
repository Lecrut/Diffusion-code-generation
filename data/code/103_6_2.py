import time

def seconds_elapsed_today():
    now = time.time()
    midnight = time.mktime(time.localtime(now))
    return int(now - midnight)

if __name__ == '__main__':
    print(seconds_elapsed_today())