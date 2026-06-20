from datetime import datetime

def time_elapsed_since_midnight():
    now = datetime.now()
    midnight = datetime.combine(now.date(), datetime.min.time())
    elapsed_time = now - midnight
    return elapsed_time.total_seconds()

if __name__ == '__main__':
    print(time_elapsed_since_midnight())