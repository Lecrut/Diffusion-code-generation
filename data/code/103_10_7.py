import datetime
SAMPLE_DATE = datetime.date(2023, 4, 1)

def time_elapsed_since_midnight():
    today = SAMPLE_DATE
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(today, datetime.time.min)
    elapsed_time = now - midnight
    return elapsed_time
if __name__ == '__main__':
    print(time_elapsed_since_midnight())