import time

def compute_elapsed_time():
    now = time.time()
    today_start = now - (now % 86400)
    elapsed_seconds = now - today_start
    hours = int(elapsed_seconds // 3600)
    remaining = elapsed_seconds - (hours * 3600)
    minutes = int(remaining // 60)
    seconds = remaining - (minutes * 60)
    return hours, minutes, seconds

if __name__ == '__main__':
    h, m, s = compute_elapsed_time()
    print(f"{h} hours, {m} minutes, {s:.2f} seconds")