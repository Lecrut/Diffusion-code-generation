import time

def get_elapsed_time():
    now = time.localtime()
    current_seconds = now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec
    hours = current_seconds // 3600
    minutes = (current_seconds % 3600) // 60
    seconds = current_seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    hours, minutes, seconds = get_elapsed_time()
    print(f"Elapsed time for the current day: {hours} hours, {minutes} minutes, and {seconds} seconds")