def both_false_checker(val_a, val_b):
    return val_a is False and val_b is False

if __name__ == '__main__':
    print(both_false_checker(False, False))
    print(both_false_checker(True, False))
    print(both_false_checker(False, True))
    print(both_false_checker(True, True))