def logical_compare(a: bool, b: bool) -> int:
    return not a and (not b) or (a and b)
if __name__ == '__main__':
    print(logical_compare(True, True))
    print(logical_compare(False, False))
    print(logical_compare(True, False))