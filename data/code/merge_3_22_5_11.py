def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or arguments
    samples = [17, -3, 42, 0]

    for num in samples:
        if is_even(num):
            print('Even')
        else:
            print('Odd')