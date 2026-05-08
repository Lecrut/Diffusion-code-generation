def are_equivalent(a: bool, b: bool) -> bool:
    return a == b
if __name__ == '__main__':
    print(are_equivalent(True, True))
    print(are_equivalent(True, False))
    print(are_equivalent(False, True))
    print(are_equivalent(False, False))