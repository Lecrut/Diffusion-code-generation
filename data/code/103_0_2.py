from datetime import datetime

def seconds_since_midnight():
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day)
    elapsed_time = now - midnight
    return elapsed_time.total_seconds()

if __name__ == '__main__':
    print(seconds_since_midnight())