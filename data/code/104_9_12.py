def check_timestamp_order(timestamp_a: float, timestamp_b: float) -> bool:
    time_point_a = timestamp_a
    time_point_b = timestamp_b
    is_earlier = time_point_a < time_point_b
    return is_earlier

if __name__ == '__main__':
    sample_first = 1700000000.5
    sample_second = 1700000001.5
    outcome = check_timestamp_order(sample_first, sample_second)
    print(outcome)