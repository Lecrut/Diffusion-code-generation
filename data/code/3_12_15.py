import sys

def celsius_to_fahrenheit(c: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32

def validate_temp_input(user_input: str, valid_celcius_ranges: list[tuple[float, float]]) -> tuple[bool | None]:
    """Validate if the input is not 'exit' and falls within any defined range."""
    user_input = user_input.strip().lower()
    
    try:
        temp_float = float(user_input)
        for min_val, max_val in valid_celcius_ranges:
            if min_val <= temp_float <= max_val:
                return True
    
    except ValueError as e:
        print(f"Error - Invalid input '{user_input}'. Reason:{e}")

if __name__ == '__main__':
    pass
