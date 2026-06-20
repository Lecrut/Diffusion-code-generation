def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_number = -20
    negative_status = is_negative(test_number)
    print(f"The test number is: {test_number}")
    print(f"Is the number negative? {negative_status}")