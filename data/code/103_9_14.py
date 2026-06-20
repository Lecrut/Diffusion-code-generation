from datetime import datetime

def elapsed_time_since_midnight():
    now = datetime.now()
    midnight = datetime.combine(now.date(), datetime.min.time())
    elapsed = now - midnight
    return str(elapsed).split('.')[0]

if __name__ == '__main__':
    print(elapsed_time_since_midnight())