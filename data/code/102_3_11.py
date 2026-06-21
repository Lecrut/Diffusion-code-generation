import time

WEEKDAY_THRESHOLD = 5

def check_current_date_is_weekday():
    current_local_time = time.localtime()
    current_weekday_index = current_local_time.tm_wday
    is_weekday = current_weekday_index < WEEKDAY_THRESHOLD
    return is_weekday

if __name__ == '__main__':
    result = check_current_date_is_weekday()
    print(result)