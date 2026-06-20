def check_both_true(a, b):
    result = a and b
    return result
if __name__ == '__main__':
    value1 = check_both_true(True, True)
    print(value1)
    value2 = check_both_true(False, False)
    print(value2)
    value3 = check_both_true(True, False)
    print(value3)
    value4 = check_both_true(False, True)
    print(value4)