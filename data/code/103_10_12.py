import datetime

def time_elapsed_since_midnight():
    hardcoded_date = datetime.datetime(2023, 4, 1)
    current_time = datetime.datetime.now()
    midnight_today = hardcoded_date.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_time = current_time - midnight_today
    return elapsed_time

if __name__ == '__main__':
    print(time_elapsed_since_midnight())