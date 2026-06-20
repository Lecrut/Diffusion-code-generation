def is_timestamp_earlier(ts1: float, ts2: float) -> bool:
    return ts1 < ts2

if __name__ == '__main__':
    timestamp_a = 1633075200.0
    timestamp_b = 1633082400.0
    result = is_timestamp_earlier(timestamp_a, timestamp_b)
    print(result)