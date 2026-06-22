def calculate_timestamp_delta(ts_first: int, ts_second: int) -> int:
    SECONDS_PER_UNIT = 1
    if not isinstance(ts_first, int) or not isinstance(ts_second, int):
        raise ValueError("Timestamps must be integers")
    delta = ts_first - ts_second
    if delta < 0:
        return -delta * SECONDS_PER_UNIT
    return delta * SECONDS_PER_UNIT

if __name__ == '__main__':
    sample_ts_a = 1672531200
    sample_ts_b = 1672531260
    calculated_delta = calculate_timestamp_delta(sample_ts_a, sample_ts_b)
    print(calculated_delta)