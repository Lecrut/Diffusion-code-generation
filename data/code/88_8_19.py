def check_both_true(a: bool, b: bool) -> bool:
    result = a and b
    return result

if __name__ == '__main__':
    sample1 = check_both_true(True, True)
    sample2 = check_both_true(False, False)
    print(sample1)
    print(sample2)