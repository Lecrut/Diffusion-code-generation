def is_odd(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n % 2 != 0

if __name__ == '__main__':
    sample_values = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for value in sample_values:
        print(f"{value} is odd: {is_odd(value)}")