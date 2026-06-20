def compare_booleans(a: bool, b: bool) -> str:
    return 'Equal' if a == b else 'Different'

if __name__ == '__main__':
    result1 = compare_booleans(True, True)
    result2 = compare_booleans(False, False)
    result3 = compare_booleans(True, False)
    result4 = compare_booleans(False, True)
    
    print(result1)
    print(result2)
    print(result3)
    print(result4)