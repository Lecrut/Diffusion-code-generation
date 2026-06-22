import datetime

SECONDS_IN_HOUR = 3600
MIDNIGHT_HOUR = 0
MIDNIGHT_MINUTE = 0
MIDNIGHT_SECOND = 0

def get_seconds_since_midnight():
    now = datetime.datetime.now()
    midnight = now.replace(
        hour=MIDNIGHT_HOUR,
        minute=MIDNIGHT_MINUTE,
        second=MIDNIGHT_SECOND,
        microsecond=0
    )
    delta = now - midnight
    return delta.total_seconds()

if __name__ == '__main__':
    elapsed_seconds = get_seconds_since_midnight()
    hours_passed = elapsed_seconds / SECONDS_IN_HOUR
    print(elapsed_seconds)
    print(hours_passed)