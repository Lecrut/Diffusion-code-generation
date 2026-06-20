def is_timestamp_before(ts1: float, ts2: float) -> bool:
    return ts1 < ts2

if __name__ == '__main__':
    print(is_timestamp_before(1633075200.0, 1633082400.0))