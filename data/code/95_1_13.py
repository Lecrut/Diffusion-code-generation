def combine_checks(first, second, third):
    if not isinstance(first, int) or not isinstance(second, int) or not isinstance(third, int):
        raise ValueError("Inputs must be integers")
    if first == 0:
        raise ValueError("First input must be non-zero for divisibility check")
    if first <= 0:
        return False
    if second % 2 != 0:
        return False
    if third % first != 0:
        return False
    return True

if __name__ == '__main__':
    result1 = combine_checks(4, 10, 20)
    print(result1)
    result2 = combine_checks(3, 5, 9)
    print(result2)
    result3 = combine_checks(0, 2, 4)
    print(result3)
    result4 = combine_checks(5, 10, 11)
    print(result4)