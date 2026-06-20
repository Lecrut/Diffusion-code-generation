from datetime import datetime

SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24

def time_elapsed_since_midnight():
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day)
    elapsed_time = now - midnight
    total_seconds = elapsed_time.days * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE + \
                    elapsed_time.seconds + elapsed_time.microseconds / 1_000_000
    return total_seconds

if __name__ == '__main__':
    print(time_elapsed_since_midnight())