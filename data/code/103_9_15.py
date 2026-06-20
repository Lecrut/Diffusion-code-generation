from datetime import datetime

def get_elapsed_time_since_midnight():
    now = datetime.now()
    midnight = datetime.combine(now.date(), datetime.min.time())
    elapsed_time = now - midnight
    return str(elapsed_time).split('.')[0]

if __name__ == '__main__':
    print(get_elapsed_time_since_midnight())