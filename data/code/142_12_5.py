def are_identical(a: bool, b: bool) -> bool:
    return a ^ b == False
if __name__ == '__main__':
    print(are_identical(True, True))
    print(are_identical(False, False))
    print(are_identical(True, False))