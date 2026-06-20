def logical_and(a: bool, b: bool) -> bool:
    return a and b
if __name__ == '__main__':
    print(logical_and(True, True))
    print(logical_and(False, True))
    print(logical_and(True, False))
    print(logical_and(False, False))