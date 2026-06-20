import time

def calculate_elapsed_time():
    start_of_day = time.mktime((time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, 0, 0, 0, 0, 0, 0))
    current_time = time.time()
    elapsed_seconds = int(current_time - start_of_day)
    hours = elapsed_seconds // 3600
    minutes = (elapsed_seconds % 3600) // 60
    seconds = elapsed_seconds % 60
    return f"{hours} hours, {minutes} minutes, and {seconds} seconds"

if __name__ == '__main__':
    print(calculate_elapsed_time())