def timestamp_difference(ts1: int, ts2: int) -> int:
    if not isinstance(ts1, int) or not isinstance(ts2, int):
        raise ValueError("Inputs must be integers")
    return abs(ts1 - ts2)

if __name__ == '__main__':
    result = timestamp_difference(1672531200, 1672531260)
    print(result)