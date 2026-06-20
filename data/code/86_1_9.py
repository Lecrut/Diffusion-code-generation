TRUE_STR = 'True'
FALSE_STR = 'False'

def compare_booleans(a, b):
    return TRUE_STR if a == b else FALSE_STR

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))
    print(compare_booleans(False, True))