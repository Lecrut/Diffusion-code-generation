import datetime

def time_elapsed_since_midnight():
    today = datetime.datetime(2023, 4, 1)
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(today, datetime.time.min)
    elapsed_time = now - midnight
    return elapsed_time.total_seconds()

if __name__ == '__main__':
    print(time_elapsed_since_midnight())