import datetime

def get_elapsed_seconds_since_midnight():
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - start_of_day
    return delta.total_seconds()

if __name__ == '__main__':
    seconds = get_elapsed_seconds_since_midnight()
    print(seconds)