def is_number_zero(num):
    return num == 0

if __name__ == '__main__':
    test_value1 = 0
    print(f"Is {test_value1} zero? {is_number_zero(test_value1)}")
    
    test_value2 = -7.5
    print(f"Is {test_value2} zero? {is_number_zero(test_value2)}")