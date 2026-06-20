import time

def elapsed_time():
    now = time.time()
    start_of_day = int(now // 86400) * 86400
    duration = now - start_of_day
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)
    return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    print(elapsed_time())