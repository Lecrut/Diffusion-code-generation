def timestamp_difference(timestamp1, timestamp2):
    return abs(timestamp1 - timestamp2)
if __name__ == '__main__':
    ts_a = 1673942400
    ts_b = 1672310400
    result = timestamp_difference(ts_a, ts_b)
    print(f'Difference between {ts_a} and {ts_b}: {result} seconds')