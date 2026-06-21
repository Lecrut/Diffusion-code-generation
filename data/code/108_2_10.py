import time

def get_current_day_of_month():
    timestamp = time.time()
    structured_time = time.localtime(timestamp)
    day_of_month = structured_time.tm_mday
    return day_of_month

def get_day_from_tuple(time_tuple):
    return time_tuple.tm_mday

if __name__ == '__main__':
    current_day = get_current_day_of_month()
    print(current_day)
    sample_tuple = time.strptime("2023-10-15", "%Y-%m-%d")
    sample_day = get_day_from_tuple(sample_tuple)
    print(sample_day)