def is_positive(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be an integer or a float")
    return number > 0

if __name__ == '__main__':
    sample_values = [42, -37, 2.718, -1.618, 0, "hello", None]
    for value in sample_values:
        try:
            result = is_positive(value)
            print(f"{value}: {result}")
        except ValueError as e:
            print(f"{value}: {e}")