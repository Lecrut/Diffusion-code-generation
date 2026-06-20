def bitwise_addition(a, b):
    while b != 0:
        carry = a & b
        a ^= b
        b = carry << 1
    return a

def standard_addition(a, b):
    return a + b

def compute_operations():
    num1 = 10
    num2 = 5
    
    if num1 < 0 or num2 < 0:
        raise ValueError("Input values must be non-negative integers.")
    
    bitwise_result = bitwise_addition(num1, num2)
    standard_result = standard_addition(num1, num2)
    
    return (bitwise_result, standard_result)

if __name__ == '__main__':
    results = compute_operations()
    print(results)