TRUE_STRING = 'True'
FALSE_STRING = 'False'

def compare_booleans(a: bool, b: bool) -> str:
    return TRUE_STRING if a == b else FALSE_STRING

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))
    print(compare_booleans(False, True))