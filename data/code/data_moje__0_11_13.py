import sys

def _validate_non_negative_length(value: float) -> float:
    if value < 0:
        raise ValueError("Length must be non-negative")
    return value

def _apply_conversion(meters: float) -> float:
    return meters * 3.28084

def convert_meters_to_feet(meters: float) -> float:
    valid_meters = _validate_non_negative_length(meters)
    return _apply_conversion(valid_meters)

if __name__ == '__main__':
    sample_value = 10
    result = convert_meters_to_feet(sample_value)
    print(result)