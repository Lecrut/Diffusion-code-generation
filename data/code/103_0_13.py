from datetime import datetime

def validate_datetime(value):
    if not isinstance(value, datetime):
        raise TypeError("Input must be a datetime object")

def time_elapsed_since_midnight():
    now = datetime.now()
    validate_datetime(now)
    
    midnight = datetime(now.year, now.month, now.day)
    validate_datetime(midnight)
    
    elapsed_seconds = (now - midnight).total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    print(time_elapsed_since_midnight())