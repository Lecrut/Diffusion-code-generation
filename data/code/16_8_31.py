def is_positive(number):
    try:
        if int(number) > 0:
            return True
        else:
            return False
    except ValueError:
        raise ValueError("Input must be an integer.")

if __name__ == '__main__':
    sample_values = [10, -5, 'a', 0, 23]
    for value in sample_values:
        try:
            result = is_positive(value)
            print(f"{value}: {result}")
        except ValueError as e:
            print(f"{value}: {e}")