def timestamp_difference(ts1: int, ts2: int) -> int:
    return abs(ts1 - ts2)
if __name__ == '__main__':
    sample_ts1 = 1674083200
    sample_ts2 = 1672492800
    result = timestamp_difference(sample_ts1, sample_ts2)
    print(f'Difference between {sample_ts1} and {sample_ts2}: {result} seconds')