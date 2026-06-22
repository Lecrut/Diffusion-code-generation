def is_first_timestamp_before_second(timestamp1: float, timestamp2: float) -> bool:
    return timestamp1 < timestamp2

if __name__ == '__main__':
    result = is_first_timestamp_before_second(1609459200.0, 1609459201.0)
    print(result)