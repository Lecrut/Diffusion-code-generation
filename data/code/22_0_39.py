def is_odd(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    return n % 2 != 0

if __name__ == '__main__':
    sample_values = [10, -3, 4, 7, 0, -8, 5]
    for value in sample_values:
        try:
            result = is_odd(value)
            print(f"{value} is odd: {result}")
        except ValueError as e:
            print(e)