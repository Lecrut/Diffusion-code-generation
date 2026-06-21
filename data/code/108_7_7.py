def get_day_from_epoch(timestamp):
    if timestamp < 0:
        raise ValueError("Timestamp must be non-negative")
    seconds_per_day = 86400
    days_since_epoch = timestamp // seconds_per_day
    day_of_month = (days_since_epoch % 30) + 1
    return day_of_month

if __name__ == '__main__':
    sample_timestamp = 1609459200
    result = get_day_from_epoch(sample_timestamp)
    print(result)