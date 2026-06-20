from datetime import datetime, time

def elapsed_time_since_midnight():
    now = datetime.now()
    midnight = datetime.combine(now.date(), time.min)
    return (now - midnight).strftime('%H:%M:%S')

if __name__ == '__main__':
    print(elapsed_time_since_midnight())