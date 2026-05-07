def combine_xor(a: bool, b: bool) -> bool:
    return a ^ b
if __name__ == '__main__':
    check1 = True
    check2 = False
    result1 = combine_xor(check1, check2)
    print(f"Check 1: {check1}, Check 2: {check2}, Result: {result1}")
    check3 = True
    check4 = True
    result2 = combine_xor(check3, check4)
    print(f"Check 3: {check3}, Check 4: {check4}, Result: {result2}")
    check5 = False
    check6 = False
    result3 = combine_xor(check5, check6)
    print(f"Check 5: {check5}, Check 6: {check6}, Result: {result3}")