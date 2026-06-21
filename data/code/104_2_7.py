def get_timestamp_difference(timestamp1: int, timestamp2: int) -> int:
    if not isinstance(timestamp1, int) or not isinstance(timestamp2, int):
        raise ValueError("Inputs must be integers")
    return abs(timestamp1 - timestamp2)

if __name__ == '__main__':
    result = get_timestamp_difference(1609459200, 1609459260)
    print(result)