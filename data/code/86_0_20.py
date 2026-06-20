def compare_booleans(a: bool, b: bool) -> str:
    return "True" if a == b else "False"

if __name__ == '__main__':
    sample1 = (True, False)
    sample2 = (False, False)
    sample3 = (True, True)

    result1 = compare_booleans(*sample1)
    result2 = compare_booleans(*sample2)
    result3 = compare_booleans(*sample3)

    print(result1)
    print(result2)
    print(result3)