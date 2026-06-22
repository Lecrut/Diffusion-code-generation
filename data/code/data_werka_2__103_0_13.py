import datetime

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
SECONDS_PER_DAY = 86400

def calculate_elapsed_seconds():
    current_time = datetime.datetime.now()
    start_of_day = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
    time_delta = current_time - start_of_day
    return time_delta.total_seconds()

if __name__ == '__main__':
    elapsed_seconds = calculate_elapsed_seconds()
    print(elapsed_seconds)