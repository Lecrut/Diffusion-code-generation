from datetime import datetime

def time_since_midnight():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight
    return delta.total_seconds()

if __name__ == '__main__':
    print(time_since_midnight())