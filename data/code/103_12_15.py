from datetime import datetime

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def calculate_elapsed_time():
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day)
    elapsed_time = now - midnight
    total_seconds = elapsed_time.total_seconds()
    hours = int(total_seconds // (HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE))
    minutes = int((total_seconds % (HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE)) 
                   // (MINUTES_PER_HOUR * SECONDS_PER_MINUTE))
    seconds = int((total_seconds % (MINUTES_PER_HOUR * SECONDS_PER_MINUTE)) // SECONDS_PER_MINUTE)
    return hours, minutes, seconds

if __name__ == '__main__':
    hours, minutes, seconds = calculate_elapsed_time()
    print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")