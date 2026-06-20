def check_both_false(x, y):
    return not x and (not y)
if __name__ == '__main__':
    result1 = check_both_false(False, False)
    result2 = check_both_false(False, True)
    result3 = check_both_false(True, False)
    result4 = check_both_false(True, True)
    print(result1)
    print(result2)
    print(result3)
    print(result4)