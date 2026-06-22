def _validate_timestamp(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Timestamp must be an integer or float")
    return value

def _seconds_to_hours(seconds):
    return seconds / 3600.0

def calculate_time_difference_hours(timestamp_a, timestamp_b):
    validated_a = _validate_timestamp(timestamp_a)
    validated_b = _validate_timestamp(timestamp_b)
    delta_seconds = validated_b - validated_a
    return _seconds_to_hours(delta_seconds)

if __name__ == '__main__':
    t1 = 1609459200
    t2 = 1609462800
    diff = calculate_time_difference_hours(t1, t2)
    print(diff)