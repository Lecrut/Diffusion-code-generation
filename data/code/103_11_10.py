from datetime import datetime

def time_since_midnight():
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day)
    return (now - midnight).total_seconds()

if __name__ == '__main__':
    print(time_since_midnight())