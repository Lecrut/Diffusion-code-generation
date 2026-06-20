def are_booleans_identical(a: bool, b: bool) -> bool:
    return a == b
if __name__ == '__main__':
    print(are_booleans_identical(True, True))
    print(are_booleans_identical(False, False))
    print(are_booleans_identical(True, False))