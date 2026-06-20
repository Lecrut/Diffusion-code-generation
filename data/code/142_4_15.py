def check_xor_difference(a: bool, b: bool) -> bool:
    return (a and not b) or (not a and b)

if __name__ == '__main__':
    print(check_xor_difference(True, False))
    print(check_xor_difference(True, True))
    print(check_xor_difference(False, False))
    print(check_xor_difference(True, True))
    print(check_xor_difference(False, True))