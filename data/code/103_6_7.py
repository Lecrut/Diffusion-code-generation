import time

SECONDS_PER_DAY = 24 * 60 * 60

def seconds_elapsed_today():
    now = time.time()
    midnight = int(now // SECONDS_PER_DAY) * SECONDS_PER_DAY
    return int(now - midnight)

if __name__ == '__main__':
    print(seconds_elapsed_today())