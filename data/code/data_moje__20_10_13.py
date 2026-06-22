def is_even(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer.")
    return (n & 1) == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, 10, -3]
    for val in sample_values:
        print(is_even(val))