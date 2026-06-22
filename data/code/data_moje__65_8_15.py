def _validate_positive(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number, got {type(value).__name__}")
    if value < 0:
        raise ValueError(f"{name} must be non-negative, got {value}")

CONVERSION_FACTOR = 12

def convert_feet_to_inches(feet):
    _validate_positive(feet, "feet")
    return feet * CONVERSION_FACTOR

if __name__ == '__main__':
    input_feet = 12
    result = convert_feet_to_inches(input_feet)
    assert result == 144, f"Expected 144, got {result}"
    print(result)