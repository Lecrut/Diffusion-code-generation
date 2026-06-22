def time_difference(timestamp1, timestamp2):
    if not isinstance(timestamp1, (int, float)) or not isinstance(timestamp2, (int, float)):
        raise ValueError("Timestamps must be numeric")
    return abs(timestamp1 - timestamp2)

if __name__ == '__main__':
    ts1 = 1609459200
    ts2 = 1609462800
    result = time_difference(ts1, ts2)
    print(result)