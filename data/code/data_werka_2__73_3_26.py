def compute_time_delta(timestamp_a: int, timestamp_b: int) -> int:
    time_units = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400
    }
    raw_diff = timestamp_a - timestamp_b
    if raw_diff < 0:
        raw_diff = -raw_diff
    return raw_diff

if __name__ == '__main__':
    start_epoch = 1609459200
    end_epoch = 1609545600
    delta_seconds = compute_time_delta(start_epoch, end_epoch)
    print(delta_seconds)