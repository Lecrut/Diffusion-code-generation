import time

def calculate_elapsed_time_today():
    now = time.time()
    midnight = time.mktime(time.localtime(now)[:3] + (0, 0, 0))
    elapsed_seconds = int(now - midnight)
    return elapsed_seconds

if __name__ == '__main__':
    print(calculate_elapsed_time_today())