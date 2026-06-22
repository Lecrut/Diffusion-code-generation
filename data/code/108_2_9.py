import time

def get_day_of_month():
    current_time = time.time()
    local_time = time.localtime(current_time)
    return local_time.tm_mday

if __name__ == '__main__':
    result = get_day_of_month()
    print(result)