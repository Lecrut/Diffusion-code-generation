from datetime import datetime

def validate_time(time):
    if time < datetime(1970, 1, 1) or time > datetime.now():
        raise ValueError("Invalid time provided")

def calculate_elapsed_seconds_since_midnight(current_time):
    midnight = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_seconds = (current_time - midnight).total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    now = datetime.now()
    validate_time(now)
    print(calculate_elapsed_seconds_since_midnight(now))