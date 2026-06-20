def check_conditions(num):
    is_positive = num > 0
    is_even = num % 2 == 0
    is_less_than_100 = num < 100
    return is_positive and is_even and is_less_than_100
if __name__ == '__main__':
    sample_value = 42
    result = check_conditions(sample_value)
    print(result)