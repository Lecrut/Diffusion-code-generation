SECONDS_PER_MINUTE = 60

def calculate_timestamp_delta(first_timestamp: int, second_timestamp: int) -> int:
    if not isinstance(first_timestamp, int) or not isinstance(second_timestamp, int):
        raise ValueError("Arguments must be integers")
    raw_delta = first_timestamp - second_timestamp
    if raw_delta < 0:
        return raw_delta * -1
    return raw_delta

if __name__ == '__main__':
    ts_start = 1672531200
    ts_end = 1672531260
    delta_seconds = calculate_timestamp_delta(ts_start, ts_end)
    print(delta_seconds)