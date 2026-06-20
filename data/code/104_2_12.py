SECONDS_PER_DAY = 86400

def seconds_difference(timestamp1: int, timestamp2: int) -> int:
    return abs(timestamp1 - timestamp2)
if __name__ == '__main__':
    ts_a = 1673980800
    ts_b = 1672304000
    diff_seconds = seconds_difference(ts_a, ts_b)
    print(f'Absolute difference in seconds between {ts_a} and {ts_b}: {diff_seconds}')