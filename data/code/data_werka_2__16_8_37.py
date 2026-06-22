def is_positive(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    return number > 0

if __name__ == '__main__':
    try:
        sample_values = [10, -5, 0, 'a', None]
        for value in sample_values:
            result = is_positive(value)
            print(f"Is {value} positive? {result}")
    except ValueError as e:
        print(e)