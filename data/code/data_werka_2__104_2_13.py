from datetime import datetime, timezone

def calculate_seconds_diff(ts_a: int, ts_b: int) -> int:
    if not isinstance(ts_a, int) or not isinstance(ts_b, int):
        raise ValueError("Both arguments must be integers")
    if ts_a == ts_b:
        return 0
    return abs(ts_a - ts_b)

if __name__ == '__main__':
    t1 = 1672531200
    t2 = 1672531260
    print(calculate_seconds_diff(t1, t2))
    t3 = 1609459200
    t4 = 1609459200
    print(calculate_seconds_diff(t3, t4))