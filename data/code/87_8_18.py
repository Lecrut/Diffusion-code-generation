def xor_check(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    result1 = xor_check(True, False)
    result2 = xor_check(False, True)
    result3 = xor_check(True, True)
    result4 = xor_check(False, False)

    print(f"xor_check(True, False) -> {result1}")
    print(f"xor_check(False, True) -> {result2}")
    print(f"xor_check(True, True) -> {result3}")
    print(f"xor_check(False, False) -> {result4}")