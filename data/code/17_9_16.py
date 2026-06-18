def is_even(number: int) -> bool:
    """Check if a given integer is even."""
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [1, -4, 63789, 0, 5]
    
    for value in test_values:
        result = "Even" if is_even(value) else "Odd"
        print(f"{value} is {result}")