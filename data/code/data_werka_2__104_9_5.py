def validate_timestamps(ts1: float, ts2: float) -> None:
    if not isinstance(ts1, (int, float)):
        raise ValueError("First timestamp must be a numeric type")
    if not isinstance(ts2, (int, float)):
        raise ValueError("Second timestamp must be a numeric type")
    if ts1 != ts1 or ts2 != ts2:
        raise ValueError("Timestamps cannot be NaN")

def is_first_timestamp_before_second(ts1: float, ts2: float) -> bool:
    validate_timestamps(ts1, ts2)
    return ts1 < ts2

if __name__ == '__main__':
    start_time = 1700000000.0
    end_time = 1700000001.0
    result = is_first_timestamp_before_second(start_time, end_time)
    print(result)