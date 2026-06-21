import datetime
import sys

def get_seconds_elapsed_since_midnight():
    now = datetime.datetime.now()
    if now.tzinfo is not None:
        raise ValueError("Current time must be naive")
    midnight = datetime.datetime.min.replace(year=now.year, month=now.month, day=now.day)
    delta = now - midnight
    return delta.total_seconds()

def main():
    seconds = get_seconds_elapsed_since_midnight()
    print(seconds)

if __name__ == '__main__':
    main()