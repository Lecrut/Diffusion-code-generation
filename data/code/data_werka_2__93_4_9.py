def determine_both_false(val1, val2):
    bool1 = not val1
    bool2 = not val2
    return bool1 and bool2

if __name__ == '__main__':
    result = determine_both_false(0, 0)
    print(result)
    result2 = determine_both_false(1, 0)
    print(result2)
    result3 = determine_both_false(None, None)
    print(result3)