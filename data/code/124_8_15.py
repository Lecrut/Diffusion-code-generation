def bitwise_add(a, b):
    while b != 0:
        carry = a & b
        a ^= b
        b = carry << 1
    return a

def standard_add(a, b):
    return a + b

def calculate_operations():
    try:
        num1 = 10
        num2 = 5
        
        add_result_bitwise = bitwise_add(num1, num2)
        add_result_standard = standard_add(num1, num2)
        
        return (add_result_bitwise, add_result_standard)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    results = calculate_operations()
    if results is not None:
        print(results)