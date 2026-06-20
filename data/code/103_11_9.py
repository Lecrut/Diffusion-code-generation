import time

def calculate_elapsed_time_today():
    now = time.time()
    start_of_day = int(now // 86400) * 86400
    elapsed_seconds = now - start_of_day
    return int(elapsed_seconds)

if __name__ == '__main__':
    print(calculate_elapsed_time_today())