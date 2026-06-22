def is_valid_positive_even(number):
    is_positive = number > 0
    is_even = number % 2 == 0
    is_less_than_100 = number < 100
    return is_positive and is_even and is_less_than_100

if __name__ == '__main__':
    test_value = 42
    result = is_valid_positive_even(test_value)
    print(result)