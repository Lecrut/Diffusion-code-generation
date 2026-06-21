import time

SECONDS_IN_DAY = 86400
TIMESTAMP_OFFSET = 0

def extract_day_from_timestamp(timestamp):
    local_time_tuple = time.localtime(timestamp)
    return local_time_tuple.tm_mday

def get_current_day():
    now = time.time()
    day = extract_day_from_timestamp(now)
    return day

if __name__ == '__main__':
    current_day = get_current_day()
    print(current_day)
    sample_timestamp = time.mktime(time.strptime("2023-01-15 12:00:00", "%Y-%m-%d %H:%M:%S"))
    sample_day = extract_day_from_timestamp(sample_timestamp)
    print(sample_day)