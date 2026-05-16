def xor(a, b):
    return a ^ b
if __name__ == '__main__':
    a = 1
    b = 0
    result = xor(a, b)
    print(f"XOR of {a} and {b} is {result}")
    a = 10
    b = 5
    result = xor(a, b)
    print(f"XOR of {a} and {b} is {result}")
    a = 11
    b = 11
    result = xor(a, b)
    print(f"XOR of {a} and {b} is {result}")