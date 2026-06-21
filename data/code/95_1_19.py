def _validate_positive(value):
    return value > 0

def _validate_even(value):
    return value % 2 == 0

def _validate_divisible(numerator, denominator):
    return numerator % denominator == 0

def combine_checks(first, second, third):
    is_first_positive = _validate_positive(first)
    is_second_even = _validate_even(second)
    is_third_divisible = _validate_divisible(third, first)
    return is_first_positive and is_second_even and is_third_divisible

if __name__ == '__main__':
    result1 = combine_checks(4, 10, 20)
    print(result1)
    result2 = combine_checks(3, 5, 9)
    print(result2)
    result3 = combine_checks(-2, 4, 8)
    print(result3)
    result4 = combine_checks(5, 8, 15)
    print(result4)