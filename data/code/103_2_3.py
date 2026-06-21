import time

def compute_elapsed_time():
    now = time.time()
    today_start = now - (now % 86400)
    elapsed_seconds = now - today_start
    hours = int(elapsed_seconds // 3600)
    remaining_seconds = elapsed_seconds % 3600
    minutes = int(remaining_seconds // 60)
    seconds = remaining_seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    result = compute_elapsed_time()
    print(result)