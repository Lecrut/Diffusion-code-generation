def calculate_timestamp_difference(timestamp1: float, timestamp2: float) -> float:
    def validate_timestamp(value: float, name: str) -> float:
        if not isinstance(value, (int, float)):
            raise ValueError(f"{name} must be a numeric type")
        if value < 0:
            raise ValueError(f"{name} cannot be negative")
        return float(value)
    
    t1 = validate_timestamp(timestamp1, "timestamp1")
    t2 = validate_timestamp(timestamp2, "timestamp2")
    
    return abs(t1 - t2)

if __name__ == '__main__':
    start_time = 1609459200.5
    end_time = 1609462800.25
    diff = calculate_timestamp_difference(start_time, end_time)
    print(diff)