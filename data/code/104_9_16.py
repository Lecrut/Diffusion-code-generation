def is_timestamp_before(ts1, ts2):
    return ts1 < ts2

if __name__ == '__main__':
    print(is_timestamp_before(1633024800.0, 1633025200.0))