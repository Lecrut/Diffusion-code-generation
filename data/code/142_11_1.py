def compare_booleans(a, b):
    if a == b:
        return 'Equal'
    elif a and not b:
        return 'One is True, the other is False'
    elif not a and b:
        return 'One is True, the other is False'
    else:
        return 'Both are False'
if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(True, False))
    print(compare_booleans(False, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))