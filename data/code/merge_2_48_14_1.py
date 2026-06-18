def safe_divide(initial_value: float | int, subsequent_value: float | int) -> float:
    if not isinstance(initial_value, (int, float)):
        raise TypeError(f"Initial value must be a number, got {type(initial_value).__name__}")
    if not isinstance(subsequent_value, (int, float)):
        raise TypeError(f"Subsequent value must be a number, got {type(subsequent_value).__name__}")
    if subsequent_value == 0:
        raise ValueError("Cannot divide by zero. Subsequent value is invalid.")
    return initial_value / subsequent_value
if __name__ == '__main__':
    init_val = 150
    div_val = -6
    try:
        result = safe_divide(init_val, div_val)
        print(f"Result of {init_val} / {div_val}: {result}")
        pos_result = safe_divide(100, 4)
        print(f"Result of 100 / 4: {pos_result}")
    except (TypeError, ValueError) as e:
        error_msg = f"{type(e).__name__}: {e}"
        print(error_msg)