import time

DAY_LOOKUP = {
    'tm_mday': 0
}

def get_day_of_month():
    now = time.localtime()
    day = now.tm_mday
    DAY_LOOKUP['tm_mday'] = day
    return day

if __name__ == '__main__':
    sample_time = time.mktime((2023, 10, 15, 12, 0, 0, 0, 0, 0))
    sample_struct = time.localtime(sample_time)
    sample_day = sample_struct.tm_mday
    current_day = get_day_of_month()
    print(current_day)
    print(sample_day)
    print(DAY_LOOKUP['tm_mday'])