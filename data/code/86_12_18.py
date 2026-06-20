def compare_booleans(a: bool, b: bool) -> str:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both arguments must be boolean values.")
    return 'Equal' if a == b else 'Not Equal'

if __name__ == '__main__':
    result1 = compare_booleans(True, True)
    print(f"Comparing {True} and {True}: {result1}")
    result2 = compare_booleans(True, False)
    print(f"Comparing {True} and {False}: {result2}")
    result3 = compare_booleans(False, True)
    print(f"Comparing {False} and {True}: {result3}")
    result4 = compare_booleans(False, False)
    print(f"Comparing {False} and {False}: {result4}")