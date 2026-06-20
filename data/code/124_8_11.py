def bitwise_addition(a, b):
    mask = 0xFFFFFFFF
    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & mask
        b = carry & mask
    return a

def standard_subtraction(a, b):
    return a - b if a >= b else b - a

def calculate_operations():
    num1 = 10
    num2 = 5
    
    add_result = bitwise_addition(num1, num2)
    subtract_result = standard_subtraction(num1, num2) if num1 > num2 else standard_subtraction(num2, num1)
    
    return (add_result, subtract_result)

if __name__ == '__main__':
    results = calculate_operations()
    print(results)