from datetime import datetime

def time_elapsed_since_midnight():
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day)
    elapsed_seconds = (now - midnight).total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    print(time_elapsed_since_midnight())