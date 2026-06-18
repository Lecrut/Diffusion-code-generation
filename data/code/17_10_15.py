def is_even(number):
    """Check if a number is even using the modulo operator."""
    return number % 2 == 0

if __name__ == '__main__':
    # Sample values to test without user input
    sample_numbers = [4, 7, -3, 10]

    for num in sample_numbers:
        if is_even(num):
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")