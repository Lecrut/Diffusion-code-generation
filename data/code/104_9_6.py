def is_time_before(ts1: float, ts2: float) -> bool:
    return ts1 < ts2

if __name__ == '__main__':
    print(is_time_before(1633072800.0, 1633072801.0))