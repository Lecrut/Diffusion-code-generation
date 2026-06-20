from datetime import datetime

def elapsed_time_since_midnight():
    now = datetime.now()
    midnight = datetime.combine(now.date(), datetime.min.time())
    return (now - midnight).strftime('%H:%M:%S')

if __name__ == '__main__':
    print(elapsed_time_since_midnight())