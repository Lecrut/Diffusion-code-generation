def validate_number(n):
    is_positive = n > 0
    is_even = n % 2 == 0
    is_within_range = n < 100
    return is_positive and is_even and is_within_range

if __name__ == '__main__':
    test_val = 42
    result = validate_number(test_val)
    print(result)