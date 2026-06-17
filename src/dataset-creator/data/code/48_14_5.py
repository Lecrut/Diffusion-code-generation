def safe_divide(initial_value: float | int, subsequent_value: float | int) -> float:
    if not isinstance(initial_value, (int, float)) or not isinstance(subsequent_value, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    if subsequent_value == 0:
        raise ValueError("Division by zero is undefined. The denominator cannot be zero.")
    return initial_value / subsequent_value
if __name__ == '__main__':
    INITIAL_VAL = 150
    SUBSEQUENT_VAL = -6
    try:
        result = safe_divide(INITIAL_VAL, SUBSEQUENT_VAL)
        print(f"Result of {INITIAL_VAL} divided by {SUBSEQUENT_VAL}: {result}")
    except (TypeError, ValueError) as e:
        print(f"An error occurred during division: {e}")