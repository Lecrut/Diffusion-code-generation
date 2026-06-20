def is_both_true(val1, val2):
    return bool(val1) and bool(val2)
if __name__ == '__main__':
    result1 = is_both_true(True, True)
    result2 = is_both_true(False, True)
    print(result1)
    print(result2)