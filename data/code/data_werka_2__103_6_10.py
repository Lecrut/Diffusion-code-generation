import time

def get_seconds_elapsed_today():
    now = time.time()
    midnight = now - (now % 86400)
    return now - midnight

if __name__ == '__main__':
    result = get_seconds_elapsed_today()
    print(result)