import time
MIDNIGHT_SECONDS = 86400

def seconds_elapsed_today():
    now = time.time()
    today_midnight = now // MIDNIGHT_SECONDS * MIDNIGHT_SECONDS
    return int(now - today_midnight)
if __name__ == '__main__':
    elapsed_seconds = seconds_elapsed_today()
    print(elapsed_seconds)