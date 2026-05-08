def check_xor_difference(a, b):
    return a ^ b
if __name__ == '__main__':
    bool1 = True
    bool2 = False
    result = check_xor_difference(bool1, bool2)
    print(result)
    bool3 = True
    bool4 = True
    result = check_xor_difference(bool3, bool4)
    print(result)
    bool5 = False
    bool6 = False
    result = check_xor_difference(bool5, bool6)
    print(result)