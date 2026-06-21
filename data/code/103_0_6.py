import datetime

def calculate_seconds_since_midnight():
    now = datetime.datetime.now()
    midnight_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight_today
    total_seconds = int(delta.total_seconds())
    return total_seconds

if __name__ == '__main__':
    result = calculate_seconds_since_midnight()
    print(result)