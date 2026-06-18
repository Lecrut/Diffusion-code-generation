def safe_divide(initial_value: float | int, subsequent_value: float | int) -> float:
    if not isinstance(initial_value, (int, float)) or not isinstance(subsequent_value, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    if subsequent_value == 0:
        raise ZeroDivisionError(f"Cannot divide by zero. Subsequent value is {subsequent_value}.")
    return initial_value / subsequent_value
if __name__ == '__main__':
    INITIAL_VALUE = 150
    SUBSEQUENT_VALUE = 6
    try:
        result = safe_divide(INITIAL_VALUE, SUBSEQUENT_VALUE)
        print(f"Result of {INITIAL_VALUE} / {SUBSEQUENT_VALUE}: {result}")
        ZERO_DIVISOR_TEST = 0
        try:
            safe_divide(INITIAL_VALUE, ZERO_DIVISOR_TEST)
        except ZeroDivisionError as e:
            print(f"Caught expected error: {e}")
    except TypeError as te:
        print(f"Input validation failed: {te}")