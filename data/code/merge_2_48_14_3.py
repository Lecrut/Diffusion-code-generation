def safe_divide(initial_value: float | int, subsequent_value: float | int) -> float:
    if not isinstance(initial_value, (int, float)) or not isinstance(subsequent_value, (int, float)):
        raise TypeError(f"Both arguments must be numeric types (int or float), got {type(initial_value).__name__} and {type(subsequent_value).__name__}")
    if subsequent_value == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return initial_value / subsequent_value
if __name__ == '__main__':
    init_val = 100.5
    sub_val = 20
    try:
        result = safe_divide(init_val, sub_val)
        print(f"Result of dividing {init_val} by {sub_val}: {result}")
    except TypeError as te:
        print(f"Type Error occurred: {te}")
    except ZeroDivisionError as ze:
        print(f"Zero Division Error occurred: {ze}")