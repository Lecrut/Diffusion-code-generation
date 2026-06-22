import time

def get_current_day():
    local_time = time.localtime()
    if local_time is None:
        raise ValueError("Time structure is invalid")
    day = local_time.tm_mday
    if not isinstance(day, int) or day < 1:
        raise ValueError("Invalid day value")
    return day

if __name__ == '__main__':
    result = get_current_day()
    print(result)