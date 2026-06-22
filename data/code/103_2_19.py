import time

def get_elapsed_time():
    now = time.time()
    start_of_day = now - (now % 86400)
    elapsed_seconds = now - start_of_day
    hours = int(elapsed_seconds // 3600)
    remaining_seconds = elapsed_seconds % 3600
    minutes = int(remaining_seconds // 60)
    seconds = int(remaining_seconds % 60)
    return hours, minutes, seconds

if __name__ == '__main__':
    hours, minutes, seconds = get_elapsed_time()
    print(f"{hours} hours, {minutes} minutes, {seconds} seconds")