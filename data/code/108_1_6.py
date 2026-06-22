def get_day_of_month(timestamp):
    import time
    if not isinstance(timestamp, (int, float)):
        raise ValueError("Timestamp must be a number")
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    time_tuple = time.gmtime(timestamp)
    return time_tuple.tm_mday

if __name__ == '__main__':
    sample_timestamp = 1609459200
    result = get_day_of_month(sample_timestamp)
    print(result)