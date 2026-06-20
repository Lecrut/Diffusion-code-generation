def is_timestamp_before(ts1: float, ts2: float) -> bool:
    if not isinstance(ts1, (int, float)) or not isinstance(ts2, (int, float)):
        raise ValueError("Both inputs must be floats or integers representing Unix timestamps.")
    
    return ts1 < ts2

if __name__ == '__main__':
    print(is_timestamp_before(1633075200.0, 1633082400.0))