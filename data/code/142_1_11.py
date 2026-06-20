def are_identical(a: bool, b: bool) -> bool:
    return not (a ^ b)

if __name__ == '__main__':
    print(are_identical(True, True))
    print(are_identical(False, False))
    print(are_identical(True, False))
    print(are_identical(False, True))