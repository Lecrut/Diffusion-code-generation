def compare_booleans(a: bool, b: bool) -> str:
    comparison_table = {True: 'Equal', False: 'Not Equal'}
    return comparison_table[a] if a == b else comparison_table[b]

if __name__ == '__main__':
    result1 = compare_booleans(True, True)
    print(result1)
    result2 = compare_booleans(True, False)
    print(result2)
    result3 = compare_booleans(False, True)
    print(result3)
    result4 = compare_booleans(False, False)
    print(result4)