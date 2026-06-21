def validate_timestamp(value: float) -> float:
    if not isinstance(value, (int, float)):
        raise ValueError("Timestamp must be a numeric type")
    if value != value:
        raise ValueError("Timestamp cannot be NaN")
    return float(value)

def is_first_timestamp_before_second(ts1: float, ts2: float) -> bool:
    validated_ts1 = validate_timestamp(ts1)
    validated_ts2 = validate_timestamp(ts2)
    return validated_ts1 < validated_ts2

if __name__ == '__main__':
    sample_ts1 = 1700000000.5
    sample_ts2 = 1700000001.5
    result = is_first_timestamp_before_second(sample_ts1, sample_ts2)
    print(result)