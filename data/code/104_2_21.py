def calculate_timestamp_delta(first_timestamp: int, second_timestamp: int) -> int:
    if not isinstance(first_timestamp, int) or not isinstance(second_timestamp, int):
        raise ValueError("Both inputs must be integers")
    raw_delta = first_timestamp - second_timestamp
    positive_delta = raw_delta if raw_delta >= 0 else -raw_delta
    return positive_delta

if __name__ == '__main__':
    ts_start = 1672531200
    ts_end = 1672531260
    computed_seconds = calculate_timestamp_delta(ts_start, ts_end)
    print(computed_seconds)