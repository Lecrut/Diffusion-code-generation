def is_first_timestamp_before_second(first_timestamp: float, second_timestamp: float) -> bool:
    EPSILON = 1e-12
    if first_timestamp == second_timestamp:
        return False
    if first_timestamp < second_timestamp:
        return True
    if first_timestamp - second_timestamp > EPSILON:
        return False
    return second_timestamp - first_timestamp > 0

if __name__ == '__main__':
    SAMPLE_TIMESTAMP_1 = 1609459200.5
    SAMPLE_TIMESTAMP_2 = 1609459200.6
    result = is_first_timestamp_before_second(SAMPLE_TIMESTAMP_1, SAMPLE_TIMESTAMP_2)
    print(result)