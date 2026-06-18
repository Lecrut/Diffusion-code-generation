def get_int(value):
    """Returns an integer from a string representation."""
    return int(value)

def is_even(number):
    """Checks if a number is even using modulo operator."""
    return number % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to avoid any input() or sys.stdin calls.
    test_cases = [4, 7, -3, 18]

    for num_str in test_cases:
        num = get_int(num_str)
        if is_even(num):
            print('Even')
        else:
            print('Odd')