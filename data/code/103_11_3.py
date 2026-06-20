from datetime import datetime

def seconds_since_midnight():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    return (now - midnight).total_seconds()

if __name__ == '__main__':
    print(seconds_since_midnight())