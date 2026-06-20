import time

def elapsed_time():
    current_time = time.time()
    start_of_day = time.mktime(time.localtime())
    elapsed_seconds = int(current_time - start_of_day)
    hours, remainder = divmod(elapsed_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours}h {minutes}m {seconds}s'
if __name__ == '__main__':
    print(elapsed_time())