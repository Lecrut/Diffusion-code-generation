import datetime

def calculate_seconds_since_midnight():
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight
    return delta.total_seconds()

if __name__ == '__main__':
    result = calculate_seconds_since_midnight()
    print(result)