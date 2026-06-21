def both_false_checker(val1, val2):
    IS_FALSE = False
    if val1 is IS_FALSE and val2 is IS_FALSE:
        yield True
    else:
        yield False

if __name__ == '__main__':
    results = list(both_false_checker(False, False))
    print(results)
    results2 = list(both_false_checker(True, False))
    print(results2)