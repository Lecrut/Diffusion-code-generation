def calculate_division(initial_value: float, subsequent_value: float) -> float | None:
    if not (isinstance(initial_value, (int, float)) and isinstance(subsequent_value, (int, float))):
        raise TypeError("Both initial_value and subsequent_value must be numbers.")
    try:
        num = float(initial_value)
        den = float(subsequent_value)
        if den == 0.0:
            raise ValueError(f"Division by zero is not allowed. Subsequent value was {den}.")
        result = num / den
    except OverflowError as e:
        print(f"Warning: Numeric overflow occurred during calculation due to extremely large/small values.")
        return None
    return result
if __name__ == '__main__':
    initial_val = 100.5
    subsequent_val = 20
    try:
        quotient = calculate_division(initial_val, subsequent_val)
        if quotient is not None:
            print(f"Result of {initial_val} / {subsequent_val}: {quotient}")
        else:
            print("Calculation failed due to numeric overflow or other internal errors.")
    except (TypeError, ValueError) as error:
        print(f"An unexpected error occurred during calculation: {error}")