from datetime import datetime

def time_elapsed_since_midnight():
    now = datetime.now()
    if now.hour < 0 or now.minute < 0 or now.second < 0 or now.microsecond < 0:
        raise ValueError("Invalid time values")
    
    midnight = datetime(now.year, now.month, now.day)
    elapsed_seconds = (now - midnight).total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    print(time_elapsed_since_midnight())