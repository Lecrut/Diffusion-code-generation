import time

def get_current_day_of_month():
    now = time.localtime()
    day = now.tm_mday
    if not isinstance(day, int) or day < 1 or day > 31:
        raise ValueError("Invalid day of month extracted from system time")
    return day

if __name__ == '__main__':
    result = get_current_day_of_month()
    print(result)