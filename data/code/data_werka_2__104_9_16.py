def is_first_before_second(timestamp1: float, timestamp2: float) -> bool:
    return timestamp1 < timestamp2

if __name__ == '__main__':
    result = is_first_before_second(1000.0, 2000.0)
    print(result)