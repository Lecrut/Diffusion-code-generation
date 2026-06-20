import time

def get_weekday(year, month, day):
    timestamp = time.mktime((year, month, day, 0, 0, 0, 0, 0, -1))
    weekday = time.localtime(timestamp).tm_wday
    return weekday

if __name__ == '__main__':
    year = 2023
    month = 1
    day = 1
    print(get_weekday(year, month, day))