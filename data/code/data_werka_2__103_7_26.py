from datetime import datetime, timedelta

def calculate_time_elapsed_since_midnight():
    now = datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed = now - start_of_day
    return elapsed

if __name__ == '__main__':
    result = calculate_time_elapsed_since_midnight()
    print(result)