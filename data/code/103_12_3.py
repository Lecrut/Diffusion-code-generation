from datetime import datetime

def hours_minutes_seconds_elapsed():
    now = datetime.now()
    midnight = datetime(now.year, now.month, now.day)
    elapsed = now - midnight
    return elapsed.seconds // 3600, (elapsed.seconds % 3600) // 60, elapsed.seconds % 60

if __name__ == '__main__':
    hours, minutes, seconds = hours_minutes_seconds_elapsed()
    print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")