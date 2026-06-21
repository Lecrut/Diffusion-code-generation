def check_positive_even_less_than_100(value):
    is_positive = value > 0
    is_even = value % 2 == 0
    is_less_than_100 = value < 100
    return is_positive and is_even and is_less_than_100

if __name__ == '__main__':
    test_value = 42
    result = check_positive_even_less_than_100(test_value)
    print(result)