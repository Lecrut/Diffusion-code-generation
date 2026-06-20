import time

def get_current_day_of_month():
    current_time = time.localtime()
    return current_time.tm_mday

if __name__ == '__main__':
    print(get_current_day_of_month())