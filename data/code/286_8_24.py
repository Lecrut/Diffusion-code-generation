def validate_input(value: float, unit: str) -> None:
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number.")
    if not isinstance(unit, str):
        raise TypeError("Unit must be a string.")
    if unit.lower().strip() not in ["km"]:
        raise ValueError("Invalid unit provided. Supported unit is 'km'.")

def convert_length(value: float, unit: str) -> float:
    validate_input(value, unit)
    return value * 0.621371

if __name__ == '__main__':
    test_cases = [
        (10.0, "km", 6.21371),
        (5.0, "km", 3.106855),
        (1.0, "km", 0.621371)
    ]
    
    for value, unit, expected in test_cases:
        result = convert_length(value, unit)
        print(f"convert_length({value}, '{unit}') = {result} (Expected: {expected})")