def are_equivalent(b1: bool, b2: bool) -> bool:
    return b1 & b2 | ~b1 & ~b2
if __name__ == '__main__':
    print(are_equivalent(True, True))
    print(are_equivalent(False, False))
    print(are_equivalent(True, False))
    print(are_equivalent(False, True))