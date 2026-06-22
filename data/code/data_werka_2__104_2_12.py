def calculate_seconds_between(timestamp_a: int, timestamp_b: int) -> int:
    if not isinstance(timestamp_a, int) or not isinstance(timestamp_b, int):
        raise ValueError("Both inputs must be integers")
    delta = timestamp_a - timestamp_b
    if delta < 0:
        delta = -delta
    return delta

if __name__ == '__main__':
    start_time = 1672531200
    end_time = 1672531500
    elapsed = calculate_seconds_between(start_time, end_time)
    print(elapsed)