def is_even(n: int) -> bool:
    """Check if an integer is even using bitwise AND operation."""
    return n & 1 == 0

if __name__ == '__main__':
    test_values = [-5, -2, 0, 3, 4]

    for value in test_values:
        result = "even" if is_even(value) else "odd"
        print(f"{value} is {result}")