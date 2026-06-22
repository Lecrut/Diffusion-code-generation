from typing import Union

INCHES_PER_FOOT: float = 12.0

def validate_and_convert(feet: float) -> float:
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a numeric type")
    if isinstance(feet, float) and (feet != feet or feet == float('inf') or feet == float('-inf')):
        raise ValueError("Input must be a finite real number")
    return feet * INCHES_PER_FOOT

def convert_feet_to_inches(feet: float) -> float:
    return validate_and_convert(feet)

if __name__ == '__main__':
    test_cases: list[float] = [0.0, 1.0, 100.25, 0.001, 555.9999]
    for val in test_cases:
        out_val: float = convert_feet_to_inches(val)
        print(out_val)