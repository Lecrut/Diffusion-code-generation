from datetime import datetime, timedelta

def get_current_fractional_day():
    now = datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    time_difference = now - start_of_day
    return time_difference.total_seconds()

if __name__ == '__main__':
    fractional_day = get_current_fractional_day()
    print(fractional_day)