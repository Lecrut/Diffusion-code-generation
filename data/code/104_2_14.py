def timestamp_difference(timestamp1, timestamp2):
    return abs(timestamp1 - timestamp2)

if __name__ == '__main__':
    ts_a = 1673958400
    ts_b = 1673962000
    diff = timestamp_difference(ts_a, ts_b)
    print(f"Timestamp difference between {ts_a} and {ts_b}: {diff} seconds")