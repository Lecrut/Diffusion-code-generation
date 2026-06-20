import time

def elapsed_time():
    now = time.time()
    start_of_day = int(now) - (int(now) % 86400)
    elapsed_seconds = int(now) - start_of_day
    hours = elapsed_seconds // 3600
    minutes = (elapsed_seconds % 3600) // 60
    seconds = elapsed_seconds % 60
    return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    print(elapsed_time())