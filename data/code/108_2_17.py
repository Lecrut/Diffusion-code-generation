import time

def get_current_day_of_month():
    current_time = time.localtime()
    return current_time.tm_mday

if __name__ == '__main__':
    day_of_month = get_current_day_of_month()
    print(day_of_month)