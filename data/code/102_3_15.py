import time

def get_current_weekday_status():
    current_time = time.localtime()
    day_of_week = current_time.tm_wday
    if not isinstance(day_of_week, int):
        raise ValueError("Expected integer day of week")
    if day_of_week < 0 or day_of_week > 6:
        raise ValueError("Invalid day of week value")
    return day_of_week < 5

if __name__ == '__main__':
    result = get_current_weekday_status()
    print(result)