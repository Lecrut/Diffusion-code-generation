def is_before(timestamp1: float, timestamp2: float) -> bool:
    return timestamp1 < timestamp2

if __name__ == '__main__':
    result = is_before(1678886400.0, 1678886500.0)
    print(result)