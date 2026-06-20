def is_negative(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a number")
    return number < 0

if __name__ == '__main__':
    test_number = -10
    print(f"The test number is: {test_number}")
    print(f"Is the number negative? {is_negative(test_number)}")