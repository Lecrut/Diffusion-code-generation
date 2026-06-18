def is_odd(n: int) -> bool:
    """Check if an integer is odd using bitwise AND operation."""
    return n & 1 == 1

if __name__ == '__main__':
    test_values = [-5, -2, 0, 3, 4, 100]
    for val in test_values:
        print(f"{val}: {is_odd(val)}")