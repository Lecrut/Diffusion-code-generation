def is_odd(n):
    """Returns True if n is odd, False otherwise."""
    return n % 2 != 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [17, -4, 0]

    for number in test_cases:
        if is_odd(number):
            print(f"{number} is odd")
        else:
            print(f"{number} is even")