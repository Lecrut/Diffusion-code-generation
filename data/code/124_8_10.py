def bitwise_add(a, b):
    while b:
        carry = a & b
        a ^= b
        b = carry << 1
    return a

def standard_add(a, b):
    return a + b

def calculate_operations():
    num1 = 10
    num2 = 5
    bitwise_result = bitwise_add(num1, num2)
    standard_result = standard_add(num1, num2)
    return (bitwise_result, standard_result)
if __name__ == '__main__':
    results = calculate_operations()
    print(results)