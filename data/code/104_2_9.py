def diff_timestamps(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    return a - b if a > b else b - a

if __name__ == '__main__':
    print(diff_timestamps(1672531200, 1672531260))
    print(diff_timestamps(1609459200, 1609459260))
    print(diff_timestamps(1700000000, 1699999940))