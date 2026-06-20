import time

def seconds_elapsed_today():
    now = time.time()
    midnight = int(now) - (int(now) % 86400)
    return now - midnight

if __name__ == '__main__':
    print(seconds_elapsed_today())