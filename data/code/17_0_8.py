def is_even(n):
    """Check if an integer n is even."""
    return n % 2 == 0

if __name__ == '__main__':
    # Sample values to test without user input or command-line arguments
    sample_numbers = [1, 2, -3, 4]

    for num in sample_numbers:
        if is_even(num):
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")