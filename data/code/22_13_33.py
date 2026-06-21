def is_odd(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    return n % 2 != 0

if __name__ == '__main__':
    sample_values = [10, -3, 4, 7, 0, -8]
    for value in sample_values:
        try:
            print(f"{value} is odd: {is_odd(value)}")
        except ValueError as e:
            print(e)