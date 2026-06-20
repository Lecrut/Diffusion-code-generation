import time

def elapsed_time():
    now = time.time()
    start_of_day = time.mktime(time.localtime(now))
    seconds_elapsed = int(now - start_of_day)
    hours = seconds_elapsed // 3600
    minutes = (seconds_elapsed % 3600) // 60
    seconds = seconds_elapsed % 60
    return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    print(elapsed_time())