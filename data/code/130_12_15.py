def is_zero(value: int) -> bool:
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")
    return value == 0

if __name__ == '__main__':
    sample_values = [10, 0, -5, 0, 3.14]
    for value in sample_values:
        try:
            result = is_zero(value)
            print(f"Checking value: {value}, Result: {result}")
        except ValueError as e:
            print(e)