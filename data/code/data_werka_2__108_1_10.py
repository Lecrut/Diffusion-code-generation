def get_day_of_month(timestamp):
    import time
    local_time = time.localtime(timestamp)
    return local_time.tm_mday

if __name__ == '__main__':
    sample_timestamp = 1609459200
    result = get_day_of_month(sample_timestamp)
    print(result)