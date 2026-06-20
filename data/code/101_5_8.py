import time

def get_weekday(year, month, day):
    timestamp = time.mktime((year, month, day, 0, 0, 0, 0, 0, -1))
    weekday = time.localtime(timestamp).tm_wday
    return weekday

if __name__ == '__main__':
    print(get_weekday(2023, 1, 1))