def check_both_true(a: bool, b: bool) -> bool:
    result = a and b
    return result
if __name__ == '__main__':
    sample1 = check_both_true(True, True)
    sample2 = check_both_true(False, False)
    sample3 = check_both_true(True, False)
    sample4 = check_both_true(False, True)
    print(sample1)
    print(sample2)
    print(sample3)
    print(sample4)