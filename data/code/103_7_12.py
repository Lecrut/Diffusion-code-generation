import datetime

def time_elapsed_since_midnight():
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date(), datetime.time.min)
    elapsed_time = now - midnight
    return elapsed_time.total_seconds()

if __name__ == '__main__':
    print(time_elapsed_since_midnight())