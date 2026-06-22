import time

def get_seconds_since_midnight():
    current_timestamp = time.time()
    local_time = time.localtime(current_timestamp)
    midnight_timestamp = time.mktime((
        local_time.tm_year,
        local_time.tm_mon,
        local_time.tm_mday,
        0,
        0,
        0,
        local_time.tm_wday,
        local_time.tm_yday,
        local_time.tm_isdst
    ))
    elapsed_seconds = current_timestamp - midnight_timestamp
    return elapsed_seconds

if __name__ == '__main__':
    sample_timestamp = 1717200000.0
    import datetime
    sample_dt = datetime.datetime.fromtimestamp(sample_timestamp)
    sample_midnight = sample_dt.replace(hour=0, minute=0, second=0, microsecond=0)
    sample_midnight_ts = sample_midnight.timestamp()
    sample_elapsed = sample_timestamp - sample_midnight_ts
    print(sample_elapsed)
    actual_elapsed = get_seconds_since_midnight()
    print(actual_elapsed)