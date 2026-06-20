def compare_booleans(a: bool, b: bool) -> tuple:
    operation = "=="
    result = a == b
    return (result, operation)

if __name__ == '__main__':
    print(compare_booleans(True, False))
    print(compare_booleans(False, False))
    print(compare_booleans(True, True))