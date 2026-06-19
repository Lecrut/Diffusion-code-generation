def is_positive(number):
    try:
        return number > 0
    except TypeError:
        raise ValueError("Input must be an integer")

if __name__ == '__main__':
    sample_values = [10, -5, 0, 'a', None]
    for value in sample_values:
        try:
            result = is_positive(value)
            print(f"{value}: {result}")
        except ValueError as e:
            print(f"{value}: {e}")