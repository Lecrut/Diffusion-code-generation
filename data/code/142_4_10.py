def xor_check(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    x = True
    y = False
    diff1 = xor_check(x, y)
    print(diff1)

    m = True
    n = True
    diff2 = xor_check(m, n)
    print(diff2)

    p = False
    q = False
    diff3 = xor_check(p, q)
    print(diff3)