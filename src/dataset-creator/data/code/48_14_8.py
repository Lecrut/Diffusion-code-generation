def safe_divide(initial_value: float, subsequent_value: float) -> float | None:
    if not isinstance(initial_value, (int, float)) or not isinstance(subsequent_value, (int, float)):
        raise TypeError("Both initial_value and subsequent_value must be numeric.")
    try:
        result = 0.0
        if subsequent_value != 0:
            result = initial_value / subsequent_value
        return result
    except OverflowError as e:
        print(f"Overflow error occurred during calculation: {e}")
        return None
if __name__ == '__main__':
    init_val = 100.5
    div_val = 2
    result = safe_divide(init_val, div_val)
    if result is not None:
        print(f"Result of dividing {init_val} by {div_val}: {result}")
    else:
        print("Division failed due to an error condition.")