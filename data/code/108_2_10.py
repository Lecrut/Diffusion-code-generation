import time

def get_day_of_month():
    now = time.localtime()
    return now.tm_mday

if __name__ == '__main__':
    print(get_day_of_month())