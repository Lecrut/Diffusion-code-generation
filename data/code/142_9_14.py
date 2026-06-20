def are_logically_identical(a: bool, b: bool) -> bool:
    return a == b
if __name__ == '__main__':
    print(are_logically_identical(True, True))
    print(are_logically_identical(False, False))
    print(are_logically_identical(True, False))