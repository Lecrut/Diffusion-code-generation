def check_both_false(a: bool, b: bool) -> bool:
    FALSE_CONSTANT = 0
    return not ((1 if a else FALSE_CONSTANT) | (1 if b else FALSE_CONSTANT))

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)
    result2 = check_both_false(True, False)
    print(result2)
    result3 = check_both_false(False, True)
    print(result3)
    result4 = check_both_false(True, True)
    print(result4)