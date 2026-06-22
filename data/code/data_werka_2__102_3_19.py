import time

def is_weekday():
    weekday_number = time.localtime().tm_wday
    return weekday_number < 5

if __name__ == '__main__':
    result = is_weekday()
    print(result)