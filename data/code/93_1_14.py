def are_both_false(a, b):
    return not a and (not b)
if __name__ == '__main__':
    result1 = are_both_false(False, False)
    result2 = are_both_false(True, False)
    result3 = are_both_false(False, True)
    result4 = are_both_false(True, True)
    print(result1)
    print(result2)
    print(result3)
    print(result4)