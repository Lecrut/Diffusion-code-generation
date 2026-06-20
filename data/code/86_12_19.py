def compare_booleans(a: bool, b: bool) -> str:
    comparison_table = {True: True, False: False}
    return "Equal" if comparison_table[a] == comparison_table[b] else "Not Equal"

if __name__ == '__main__':
    result1 = compare_booleans(True, True)
    print(f"Comparing {True} and {True}: {result1}")
    result2 = compare_booleans(True, False)
    print(f"Comparing {True} and {False}: {result2}")
    result3 = compare_booleans(False, True)
    print(f"Comparing {False} and {True}: {result3}")
    result4 = compare_booleans(False, False)
    print(f"Comparing {False} and {False}: {result4}")