import time

def get_current_weekday_status():
    local_time = time.localtime()
    weekday_index = local_time.tm_wday
    if weekday_index < 0 or weekday_index > 6:
        raise ValueError("Invalid weekday index returned by time module")
    return weekday_index < 5

if __name__ == '__main__':
    status = get_current_weekday_status()
    print(status)