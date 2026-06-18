def is_even(number: int) -> bool:
    """Check if a given integer is even."""
    return number % 2 == 0

if __name__ == '__main__':
    # Sample values to test the logic without user input or external dependencies.
    sample_values = [4, 5, -3, 10]

    for num in sample_values:
        if is_even(num):
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")