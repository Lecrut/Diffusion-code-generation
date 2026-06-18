# Check if an integer is odd using modulo operator
is_odd = lambda num: num % 2 != 0

if __name__ == '__main__':
    # Hard-coded sample value as requested (no user input)
    test_num = 17
    result = is_odd(test_num)
    print(f"The number {test_num} {'is' if result else 'is not'} odd.")