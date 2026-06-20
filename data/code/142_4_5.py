def xor_difference(a, b):
    return bool(a ^ b)
if __name__ == '__main__':
    bool1 = False
    bool2 = True
    result = xor_difference(bool1, bool2)
    print(result)
    bool3 = True
    bool4 = False
    result = xor_difference(bool3, bool4)
    print(result)
    bool5 = True
    bool6 = True
    result = xor_difference(bool5, bool6)
    print(result)
    bool7 = False
    bool8 = False
    result = xor_difference(bool7, bool8)
    print(result)