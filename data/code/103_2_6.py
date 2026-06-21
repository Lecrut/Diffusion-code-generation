import time

def get_elapsed_time_since_midnight():
    now = time.time()
    start_of_day = now - (now % 86400)
    elapsed_seconds = now - start_of_day
    hours = int(elapsed_seconds // 3600)
    minutes = int((elapsed_seconds % 3600) // 60)
    seconds = int(elapsed_seconds % 60)
    return hours, minutes, seconds

if __name__ == '__main__':
    h, m, s = get_elapsed_time_since_midnight()
    print(f"{h} hours, {m} minutes, {s} seconds")