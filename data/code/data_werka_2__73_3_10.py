def time_difference(t1: int, t2: int) -> int:
    return abs(t1 - t2)

if __name__ == '__main__':
    result = time_difference(1609459200, 1609459260)
    print(result)