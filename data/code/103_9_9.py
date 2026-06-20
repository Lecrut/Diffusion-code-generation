from datetime import datetime, time

def elapsed_time_since_midnight():
    now = datetime.now()
    midnight = datetime.combine(now.date(), time.min)
    elapsed = now - midnight
    return str(elapsed).split('.')[0]

if __name__ == '__main__':
    print(elapsed_time_since_midnight())