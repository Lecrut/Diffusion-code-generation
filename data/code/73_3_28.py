def time_difference(timestamp1: int, timestamp2: int) -> int:
    return abs(timestamp1 - timestamp2)

if __name__ == '__main__':
    result = time_difference(1609459200, 1609459260)
    print(result)