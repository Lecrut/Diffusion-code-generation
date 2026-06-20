from datetime import datetime

def milliseconds_since_midnight():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight
    return int(delta.total_seconds() * 1000)

if __name__ == '__main__':
    print(milliseconds_since_midnight())