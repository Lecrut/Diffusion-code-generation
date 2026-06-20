def is_number_zero(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be an integer or float.")
    return number == 0

if __name__ == '__main__':
    test_value1 = 0
    print(f"Is {test_value1} zero? {is_number_zero(test_value1)}")
    test_value2 = -5.0
    print(f"Is {test_value2} zero? {is_number_zero(test_value2)}")