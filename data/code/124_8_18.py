def bitwise_add(a, b):
    while b != 0:
        carry = a & b
        a ^= b
        b <<= 1
    return a

def standard_add(a, b):
    return a + b

def calculate_operations():
    result_bitwise = bitwise_add(10, 5)
    result_standard = standard_add(10, 5)
    return (result_bitwise, result_standard)

if __name__ == '__main__':
    results = calculate_operations()
    print(results)