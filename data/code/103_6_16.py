import time

def calculate_seconds_elapsed_today():
    current_time = time.time()
    midnight_today = int(time.mktime((time.localtime(current_time)[:3] + (0, 0, 0) + time.localtime(current_time)[6:])))
    return int(current_time - midnight_today)

if __name__ == '__main__':
    sample_timestamp = time.mktime((2023, 10, 27, 14, 30, 0, 0, 0, 0))
    elapsed_seconds = calculate_seconds_elapsed_today()
    print(elapsed_seconds)