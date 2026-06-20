from datetime import datetime

def calculate_milliseconds_since_midnight():
    now = datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    time_difference = now - start_of_day
    return int(time_difference.total_seconds() * 1000)

if __name__ == '__main__':
    milliseconds = calculate_milliseconds_since_midnight()
    print(milliseconds)