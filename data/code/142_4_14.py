def check_xor_difference(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return a ^ b

if __name__ == '__main__':
    print(check_xor_difference(True, False))
    print(check_xor_difference(True, True))
    print(check_xor_difference(False, False))
    print(check_xor_difference(True, True))
    print(check_xor_difference(False, True))