# Check if an integer is odd using bitwise AND with 1
is_odd = lambda num: (num & 1) == 1

if __name__ == '__main__':
    # Hard-coded sample value as per instructions
    test_num = 17
    result = is_odd(test_num)
    print(f"The number {test_num} {'is' if result else 'is not'} odd.")