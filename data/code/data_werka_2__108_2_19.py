import time
def extract_day_from_timestamp():
    epoch_seconds = time.time()
    local_time_struct = time.localtime(epoch_seconds)
    day_component = local_time_struct.tm_mday
    return day_component
if __name__ == '__main__':
    computed_day = extract_day_from_timestamp()
    print(computed_day)
    sample_timestamp = 1697328000.0
    sample_struct = time.localtime(sample_timestamp)
    sample_day = sample_struct.tm_mday
    print(sample_day)