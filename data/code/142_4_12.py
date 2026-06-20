def xor_helper(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values")
    return a ^ b

if __name__ == '__main__':
    result1 = xor_helper(True, False)
    print(result1)
    result2 = xor_helper(False, True)
    print(result2)
    result3 = xor_helper(True, True)
    print(result3)
    result4 = xor_helper(False, False)
    print(result4)