def compare_numbers(a, b):
    diff = a - b
    sign_bit = (diff >> 31) & 1
    return not sign_bit

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result1 = 'Greater' if compare_numbers(num1, num2) else 'Less or Equal'
    print(f"Comparing {num1} and {num2}: {result1}")
    
    num3 = 7
    num4 = 7
    result2 = 'Greater' if compare_numbers(num3, num4) else 'Less or Equal'
    print(f"Comparing {num3} and {num4}: {result2}")