def logical_equivalence(a: bool, b: bool) -> bool:
    return a & b | ~a & ~b
if __name__ == '__main__':
    print(logical_equivalence(True, True))
    print(logical_equivalence(True, False))
    print(logical_equivalence(False, False))
    print(logical_equivalence(False, True))