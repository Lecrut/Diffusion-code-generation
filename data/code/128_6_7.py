def is_negative(number: float) -> bool:
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a number")
    return number < 0

if __name__ == '__main__':
    test_values = [5.0, -1.0, 0.0, -0.001, 100.5]
    for val in test_values:
        try:
            result = is_negative(val)
            print(f"is_negative({val}) is {result}")
        except ValueError as e:
            print(e)