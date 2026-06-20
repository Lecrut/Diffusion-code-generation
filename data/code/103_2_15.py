import time

def get_elapsed_time_since_midnight():
    current_time = time.time()
    start_of_day = int(time.mktime((time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, 0, 0, 0, 0, 0, 0)))
    elapsed_seconds = current_time - start_of_day
    hours, remainder = divmod(int(elapsed_seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    elapsed = get_elapsed_time_since_midnight()
    print(f"Elapsed time since midnight: {elapsed}")