import time

def is_weekday():
    weekday_index = time.localtime().tm_wday
    return weekday_index < 5

if __name__ == '__main__':
    result = is_weekday()
    print(result)