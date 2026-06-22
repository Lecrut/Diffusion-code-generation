def compute_timestamp_gap(ts_a: int, ts_b: int) -> int:
    if not isinstance(ts_a, int) or not isinstance(ts_b, int):
        raise ValueError("Both arguments must be integers")
    offset = ts_a - ts_b
    gap = offset if offset >= 0 else -offset
    return gap

if __name__ == '__main__':
    val_one = 1700000000
    val_two = 1699999940
    diff = compute_timestamp_gap(val_one, val_two)
    print(diff)