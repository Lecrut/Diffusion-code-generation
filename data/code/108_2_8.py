import time

def get_current_day_of_month():
    return time.localtime().tm_mday

if __name__ == '__main__':
    print(get_current_day_of_month())