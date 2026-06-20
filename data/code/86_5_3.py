def compare_booleans(a: bool, b: bool) -> tuple:
    return (a == b), '=='

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)