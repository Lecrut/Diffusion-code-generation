import datetime

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

def calculate_seconds_since_midnight():
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight
    return delta.total_seconds()

if __name__ == '__main__':
    seconds_elapsed = calculate_seconds_since_midnight()
    print(seconds_elapsed)