def xor_check(a: bool, b: bool) -> bool:
    return a != b
if __name__ == '__main__':
    print(xor_check(True, False))
    print(xor_check(False, True))
    print(xor_check(True, True))
    print(xor_check(False, False))