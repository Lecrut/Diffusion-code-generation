def logical_comparison(a: bool, b: bool) -> int:
    return (not a and not b) or (a and b)

if __name__ == '__main__':
    print(logical_comparison(True, True))
    print(logical_comparison(True, False))
    print(logical_comparison(False, False))
    print(logical_comparison(False, True))