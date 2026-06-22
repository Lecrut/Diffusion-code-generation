def is_first_timestamp_before_second(ts1: float, ts2: float) -> bool:
    return ts1 < ts2

if __name__ == '__main__':
    result = is_first_timestamp_before_second(1609459200.0, 1609459201.0)
    print(result)