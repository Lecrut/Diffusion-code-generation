from datetime import datetime

def time_elapsed_since_midnight():
    today = datetime(2023, 10, 5)
    now = datetime.now()
    elapsed_time = now - today.replace(hour=0, minute=0, second=0, microsecond=0)
    return elapsed_time
if __name__ == '__main__':
    print(time_elapsed_since_midnight())