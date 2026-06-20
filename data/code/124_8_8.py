def bitwise_add(a, b):
    while b != 0:
        carry = a & b
        a ^= b
        b = carry << 1
    return a

def standard_add(a, b):
    return a + b

if __name__ == '__main__':
    result_bitwise = bitwise_add(10, 5)
    result_standard = standard_add(10, 5)
    print((result_bitwise, result_standard))