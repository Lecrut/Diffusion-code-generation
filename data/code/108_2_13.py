import time

def get_day_of_month():
    current_time = time.localtime()
    day_of_month = current_time.tm_mday
    return day_of_month

if __name__ == '__main__':
    sample_day = get_day_of_month()
    print(sample_day)