from datetime import datetime

def calculate_elapsed_time():
    now = datetime.now()
    if now.hour < 0 or now.minute < 0 or now.second < 0:
        raise ValueError("Invalid time values")
    midnight = datetime(now.year, now.month, now.day)
    elapsed_seconds = (now - midnight).total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    try:
        print(calculate_elapsed_time())
    except ValueError as e:
        print(e)