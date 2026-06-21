def _is_positive(val):
    return val > 0

def _is_even(val):
    return val % 2 == 0

def _is_divisible_by(val, divisor):
    return val % divisor == 0

def combine_checks(first, second, third):
    if not _is_positive(first):
        return False
    if not _is_even(second):
        return False
    if not _is_divisible_by(third, first):
        return False
    return True

if __name__ == '__main__':
    print(combine_checks(4, 6, 12))
    print(combine_checks(3, 4, 9))
    print(combine_checks(-2, 4, 8))
    print(combine_checks(5, 5, 10))
    print(combine_checks(2, 8, 16))