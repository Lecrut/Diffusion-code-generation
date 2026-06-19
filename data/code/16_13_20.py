def is_positive(number):
    if isinstance(number, (int, float)):
        return number > 0
    else:
        raise ValueError("Input must be an integer or a float")

if __name__ == '__main__':
    sample_values = [10, -5, 3.14, -2.71, 0, 'string']
    for value in sample_values:
        try:
            print(f"{value}: {is_positive(value)}")
        except ValueError as e:
            print(f"{value}: {e}")