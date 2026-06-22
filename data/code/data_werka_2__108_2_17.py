import time

def get_day_of_month():
    current_time = time.time()
    local_time = time.localtime(current_time)
    day = local_time.tm_mday
    return day

if __name__ == '__main__':
    result = get_day_of_month()
    print(result)