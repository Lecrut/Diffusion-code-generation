import datetime
TODAY_START = datetime.datetime(2023, 4, 1)

def calculate_time_elapsed():
    now = datetime.datetime.now()
    midnight = TODAY_START.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_time = now - midnight
    return elapsed_time
if __name__ == '__main__':
    print(calculate_time_elapsed())