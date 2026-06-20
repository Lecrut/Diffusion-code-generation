from datetime import datetime
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

def calculate_elapsed_time():
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day)
    elapsed = now - midnight
    total_seconds = elapsed.total_seconds()
    hours = int(total_seconds // (SECONDS_PER_MINUTE * MINUTES_PER_HOUR))
    minutes = int(total_seconds % (SECONDS_PER_MINUTE * MINUTES_PER_HOUR) // SECONDS_PER_MINUTE)
    seconds = int(total_seconds % SECONDS_PER_MINUTE)
    return (hours, minutes, seconds)
if __name__ == '__main__':
    hours, minutes, seconds = calculate_elapsed_time()
    print(f'{hours} hours, {minutes} minutes, and {seconds} seconds')