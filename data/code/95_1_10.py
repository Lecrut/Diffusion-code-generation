def combine_checks(first, second, third):
    threshold = 0
    is_positive = first > threshold
    is_even = second % 2 == 0
    is_divisible = third % first == 0
    return is_positive and is_even and is_divisible

if __name__ == '__main__':
    result1 = combine_checks(4, 6, 12)
    print(result1)
    result2 = combine_checks(3, 5, 12)
    print(result2)
    result3 = combine_checks(-2, 4, 8)
    print(result3)
    result4 = combine_checks(2, 3, 6)
    print(result4)