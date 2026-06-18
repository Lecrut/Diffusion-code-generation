def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or command-line arguments
    samples = [1, 2, -3, 4]

    for num in samples:
        if is_even(num):
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")