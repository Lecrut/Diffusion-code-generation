def is_odd(num):
    return num % 2 != 0

if __name__ == '__main__':
    test_number = 17
    odd_check_result = is_odd(test_number)
    print(f"Is {test_number} odd? {odd_check_result}")