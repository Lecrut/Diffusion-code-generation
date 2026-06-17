def safe_divide(initial_value, subsequent_value):
    if not (isinstance(initial_value, (int, float)) and 
            isinstance(subsequent_value, (int, float))):
        raise TypeError("Both arguments must be numeric types (int or float).")
    if subsequent_value == 0:
        raise ValueError("Cannot divide by zero. Subsequent value cannot be null.")
    return initial_value / subsequent_value
if __name__ == '__main__':
    init_val = 150
    div_val = 6
    try:
        result = safe_divide(init_val, div_val)
        print(f"Result of {init_val} / {div_val}: {result}")
        test_zero_result = safe_divide(10, 0)
    except (TypeError, ValueError) as e:
        print(f"Error occurred during calculation: {e}")