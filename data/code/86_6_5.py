def compare_booleans(a: bool, b: bool) -> tuple[bool, str]:
    operations = {
        True: "is",
        False: "is not"
    }
    result = operations[a] == operations[b]
    operation = f"{a} {operations[a]} {b}"
    return result, operation

if __name__ == '__main__':
    bool1, bool2 = True, True
    result, op = compare_booleans(bool1, bool2)
    print(f"Comparing {bool1} and {bool2}: Result={result}, Operation='{op}'")

    bool3, bool4 = True, False
    result, op = compare_booleans(bool3, bool4)
    print(f"Comparing {bool3} and {bool4}: Result={result}, Operation='{op}'")

    bool5, bool6 = False, False
    result, op = compare_booleans(bool5, bool6)
    print(f"Comparing {bool5} and {bool6}: Result={result}, Operation='{op}'")