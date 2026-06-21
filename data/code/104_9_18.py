def check_timestamp_order(first_ts: float, second_ts: float) -> bool:
    if not isinstance(first_ts, (int, float)):
        raise TypeError("first_ts must be a numeric timestamp")
    if not isinstance(second_ts, (int, float)):
        raise TypeError("second_ts must be a numeric timestamp")
    try:
        import calendar
        calendar.timegm((0, 0, 0, 0, 0, int(first_ts), 0, 0, -1))
        calendar.timegm((0, 0, 0, 0, 0, int(second_ts), 0, 0, -1))
    except (OverflowError, ValueError) as e:
        raise ValueError(f"Invalid timestamp value: {e}")
    return float(first_ts) < float(second_ts)

if __name__ == '__main__':
    t1 = 1700000000.5
    t2 = 1700000000.6
    outcome = check_timestamp_order(t1, t2)
    print(outcome)