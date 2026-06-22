import time

def is_weekday():
    weekday_index = time.localtime().tm_wday
    if weekday_index < 5:
        return True
    return False

if __name__ == '__main__':
    print(is_weekday())