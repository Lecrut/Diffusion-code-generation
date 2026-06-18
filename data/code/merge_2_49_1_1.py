def get_sign(value):
    try:
        if isinstance(value, (int, float)):
            return 1 if value > 0 else (-1 if value < 0 else 0)
        raise TypeError(f"Invalid type {type(value).__name__}")
    except Exception as e:
        print(e)
if __name__ == '__main__':
    test_values = [5, -3.2, 0, "invalid", None]
    for val in test_values:
        result = get_sign(val)
        if isinstance(result, int):
            print(f"Sign of {val}: {result}")