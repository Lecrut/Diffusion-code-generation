def compare_booleans(a: bool, b: bool) -> tuple[bool, str]:
    result = a == b
    operation = "==" if result else "!="
    return (result, operation)

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(True, False))
    print(compare_booleans(False, False))
    print(compare_booleans(False, True))