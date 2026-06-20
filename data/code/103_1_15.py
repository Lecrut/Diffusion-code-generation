from datetime import datetime

def milliseconds_since_midnight():
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day)
    return (now - midnight).total_seconds() * 1000

if __name__ == '__main__':
    print(milliseconds_since_midnight())