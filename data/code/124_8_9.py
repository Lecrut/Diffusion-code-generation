def bitwise_add(a, b):
    while b != 0:
        carry = a & b
        a ^= b
        b = carry << 1
    return a

if __name__ == '__main__':
    result = (bitwise_add(10, 5), 10 + 5)
    print(result)