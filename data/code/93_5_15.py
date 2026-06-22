def both_false_checker(a, b):
    FALSE_VAL = False
    if a is FALSE_VAL and b is FALSE_VAL:
        yield True
    else:
        yield False

if __name__ == '__main__':
    result = list(both_false_checker(False, False))
    print(result)
    result2 = list(both_false_checker(True, False))
    print(result2)
    result3 = list(both_false_checker(False, True))
    print(result3)
    result4 = list(both_false_checker(True, True))
    print(result4)