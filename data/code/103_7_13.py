import datetime

def time_elapsed_since_midnight():
    now = datetime.datetime.now()
    start_of_day = datetime.datetime.combine(now.date(), datetime.time.min)
    elapsed_time = now - start_of_day
    return elapsed_time.total_seconds()

if __name__ == '__main__':
    print(time_elapsed_since_midnight())