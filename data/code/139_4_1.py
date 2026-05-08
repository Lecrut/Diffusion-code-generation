def xor(a, b):
    return a ^ b
if __name__ == '__main__':
    a_val = 1
    b_val = 0
    result = xor(a_val, b_val)
    print(f"XOR of {a_val} and {b_val} is: {result}")
    a_val = 10
    b_val = 5
    result = xor(a_val, b_val)
    print(f"XOR of {a_val} and {b_val} is: {result}")
    a_val = 11
    b_val = 11
    result = xor(a_val, b_val)
    print(f"XOR of {a_val} and {b_val} is: {result}")