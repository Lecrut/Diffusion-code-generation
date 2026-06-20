import time

WEEKDAY_LIMIT = 5

def is_weekday():
    current_time = time.localtime()
    return current_time.tm_wday < WEEKDAY_LIMIT

if __name__ == '__main__':
    print(is_weekday())