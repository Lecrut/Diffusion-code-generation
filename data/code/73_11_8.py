def time_difference_hours(timestamp1, timestamp2):
    if not isinstance(timestamp1, (int, float)) or not isinstance(timestamp2, (int, float)):
        raise ValueError("Timestamps must be numeric")
    diff_seconds = abs(timestamp1 - timestamp2)
    return diff_seconds / 3600.0

if __name__ == '__main__':
    ts1 = 1609459200.0
    ts2 = 1609462800.0
    result = time_difference_hours(ts1, ts2)
    print(result)