def determine_sign(value):
    try:
        if isinstance(value, (int, float)):
            return 1 if value > 0 else (-1 if value < 0 else 0)
        raise TypeError("Input must be a number")
    except Exception as e:
        print(f"Error processing input {value}: {e}")
        return None
if __name__ == '__main__':
    test_values = [5, -3.2, 0, "invalid", None]
    for val in test_values:
        result = determine_sign(val)
        print(f"Sign of {val} is {result}")