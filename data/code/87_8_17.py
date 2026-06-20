def validate_inputs(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values")

def xor_check(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return a ^ b

if __name__ == '__main__':
    print(xor_check(True, False))
    print(xor_check(False, True))
    print(xor_check(True, True))
    print(xor_check(False, False))