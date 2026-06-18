def is_even(n: int) -> bool:
    """Check if an integer is even using bitwise AND operator."""
    return n & 1 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [4, -3, 0, 256, -8]

    print("Testing is_even function:")
    for num in test_values:
        result = is_even(num)
        status = "Even" if result else "Odd"
        print(f"{num} -> {status}")