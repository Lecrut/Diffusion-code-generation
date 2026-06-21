import time

WEEKDAY_LIMIT = 5

def check_is_weekday():
    current_time = time.localtime()
    return current_time.tm_wday < WEEKDAY_LIMIT

if __name__ == '__main__':
    result = check_is_weekday()
    print(result)