def is_number_odd(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    return number % 2 != 0

if __name__ == '__main__':
    sample_values = [2, -3, 4, -5, 0]
    for value in sample_values:
        print(f"{value}: {is_number_odd(value)}")