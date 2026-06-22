import time

def get_weekday_status():
    current_time = time.localtime()
    weekday_index = current_time.tm_wday
    if weekday_index < 0 or weekday_index > 6:
        raise ValueError("Invalid weekday index")
    return weekday_index < 5

if __name__ == '__main__':
    status = get_weekday_status()
    print(status)