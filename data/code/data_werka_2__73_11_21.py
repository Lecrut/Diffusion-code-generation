def _validate_timestamp(value):
    if isinstance(value, bool):
        raise ValueError("Timestamps must be numeric, not boolean")
    if not isinstance(value, (int, float)):
        raise ValueError("Timestamps must be numeric")

def calculate_time_difference_hours(timestamp_a, timestamp_b):
    _validate_timestamp(timestamp_a)
    _validate_timestamp(timestamp_b)
    seconds_delta = timestamp_b - timestamp_a
    return seconds_delta / 3600.0

if __name__ == '__main__':
    start_ts = 1609459200
    end_ts = 1609462800
    diff = calculate_time_difference_hours(start_ts, end_ts)
    print(diff)