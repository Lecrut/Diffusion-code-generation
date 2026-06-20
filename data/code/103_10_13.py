from datetime import datetime

def time_elapsed_since_midnight():
    today = datetime(2023, 4, 1)
    now = datetime.now()
    midnight = datetime.combine(today, datetime.min.time())
    elapsed_time = now - midnight
    return elapsed_time.total_seconds()

if __name__ == '__main__':
    print(time_elapsed_since_midnight())