def safe_divide(initial_value, divisor):
    if not isinstance(initial_value, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    try:
        result = initial_value / divisor
        return result
    except ZeroDivisionError as e:
        raise ZeroDivisionError(f"Cannot divide by zero. Divisor value was {divisor}.")
if __name__ == '__main__':
    initial_val = 100
    divisor_val = 4
    try:
        quotient = safe_divide(initial_val, divisor_val)
        print(f"Result of {initial_val} divided by {divisor_val}: {quotient}")
        test_zero_case = True
        if test_zero_case:
            try:
                result_zero = safe_divide(10, 0)
            except ZeroDivisionError as e:
                print(f"Caught expected exception during zero-division attempt: {e}")
    except TypeError as te:
        print(f"Input validation error occurred: {te}")