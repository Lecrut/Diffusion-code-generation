def combine_xor(a: bool, b: bool) -> bool:
    return a ^ b
if __name__ == '__main__':
    check1 = True
    check2 = False
    result1 = combine_xor(check1, check2)
    print(f"XOR({check1}, {check2}) = {result1}")
    check3 = True
    check4 = True
    result2 = combine_xor(check3, check4)
    print(f"XOR({check3}, {check4}) = {result2}")
    check5 = False
    check6 = False
    result3 = combine_xor(check5, check6)
    print(f"XOR({check5}, {check6}) = {result3}")