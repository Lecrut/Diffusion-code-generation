def is_even(n):
    """Check if an integer n is even."""
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, or args)
    test_values = [1, 2, -3, 4]

    for num in test_values:
        if is_even(num):
            print('Even')
        else:
            print('Odd')