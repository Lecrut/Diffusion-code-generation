def _check_positive(value):
    return value > 0

def _check_even(value):
    return value % 2 == 0

def _check_divisible(dividend, divisor):
    return divisor != 0 and dividend % divisor == 0

def combine_checks(first, second, third):
    is_first_positive = _check_positive(first)
    is_second_even = _check_even(second)
    is_third_divisible = _check_divisible(third, first)
    return is_first_positive and is_second_even and is_third_divisible

if __name__ == '__main__':
    result1 = combine_checks(4, 6, 12)
    print(result1)
    result2 = combine_checks(3, 5, 15)
    print(result2)
    result3 = combine_checks(-2, 4, 8)
    print(result3)
    result4 = combine_checks(2, 3, 6)
    print(result4)
    result5 = combine_checks(5, 10, 20)
    print(result5)