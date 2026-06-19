def is_positive(number):
    if isinstance(number, (int, float)):
        return number > 0
    else:
        raise ValueError("Input must be an integer or a float")

if __name__ == '__main__':
    sample_values = [10, -5, 3.14, -2.71, 0, 'string', None]
    for value in sample_values:
        try:
            result = is_positive(value)
            print(f"{value}: {result}")
        except ValueError as e:
            print(f"{value}: {e}")