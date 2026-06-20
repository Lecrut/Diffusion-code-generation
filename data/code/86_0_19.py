TRUE_RESULT = 'True'
FALSE_RESULT = 'False'

def compare_booleans(a: bool, b: bool) -> str:
    return TRUE_RESULT if a == b else FALSE_RESULT
if __name__ == '__main__':
    print(compare_booleans(True, False))
    print(compare_booleans(False, False))
    print(compare_booleans(True, True))