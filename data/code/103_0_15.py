from datetime import datetime

def time_elapsed_since_midnight():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_time = (now - midnight).total_seconds()
    return elapsed_time

if __name__ == '__main__':
    print(time_elapsed_since_midnight())