def compare_booleans(a: bool, b: bool) -> (bool, str):
    result = a == b
    operation = "==" if result else "!="
    return result, operation

if __name__ == '__main__':
    print(compare_booleans(True, False))
    print(compare_booleans(False, False))