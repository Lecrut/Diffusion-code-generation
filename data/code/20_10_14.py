def is_even_bitwise(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer")
    return (n & 1) == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, -1, -2, 100, 99]
    for val in test_values:
        print(f"is_even_bitwise({val}) = {is_even_bitwise(val)}")