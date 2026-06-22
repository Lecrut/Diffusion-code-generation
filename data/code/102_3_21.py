import time

def is_weekday():
    return time.localtime().tm_wday < 5

if __name__ == '__main__':
    result = is_weekday()
    print(result)