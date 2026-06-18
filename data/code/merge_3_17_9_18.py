def is_even(n: int) -> bool:
    """Check if an integer is even using bitwise AND operator."""
    return (n & 1) == 0

if __name__ == '__main__':
    test_values = [-5, -4, 3, 28, 99]

    for num in test_values:
        result = "Even" if is_even(num) else "Odd"
        print(f"{num} is {result}")