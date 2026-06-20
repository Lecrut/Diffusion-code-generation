def extract_day_of_month(timestamp):
    if not isinstance(timestamp, int) or timestamp < 0:
        raise ValueError("Invalid Unix epoch timestamp")
    
    seconds_per_day = 24 * 60 * 60
    day_offset = timestamp // seconds_per_day
    
    return (day_offset % 31) + 1

if __name__ == '__main__':
    sample_timestamps = [1672531200, 1682592000, 1692670400]
    for ts in sample_timestamps:
        print(extract_day_of_month(ts))