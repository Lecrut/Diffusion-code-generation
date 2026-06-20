def compare_booleans(a: bool, b: bool) -> str:
    return "True" if a == b else "False"

if __name__ == '__main__':
    result1 = compare_booleans(True, True)
    print(result1)

    result2 = compare_booleans(False, False)
    print(result2)

    result3 = compare_booleans(True, False)
    print(result3)