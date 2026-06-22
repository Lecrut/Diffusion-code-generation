def is_odd(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n % 2 != 0

if __name__ == '__main__':
    sample_values = [10, 15, -3, 8, 0, -7]
    for value in sample_values:
        print(is_odd(value))