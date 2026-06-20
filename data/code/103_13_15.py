import time

def calculate_fractional_day():
    now = time.localtime()
    start_of_day = time.mktime((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, 0, 0, -1))
    elapsed_seconds = time.time() - start_of_day
    total_seconds_in_day = 24 * 60 * 60
    fractional_part = elapsed_seconds / total_seconds_in_day
    return fractional_part

if __name__ == '__main__':
    print(calculate_fractional_day())