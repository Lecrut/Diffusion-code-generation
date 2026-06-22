def compare_numbers(a, b):
    diff = a - b
    sign_bit = (diff >> 31) & 1
    return not sign_bit

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result1 = compare_numbers(num1, num2)
    print(f"Comparing {num1} and {num2}: {'>' if result1 else '<'}")
    
    num3 = 7
    num4 = 7
    result2 = compare_numbers(num3, num4)
    print(f"Comparing {num3} and {num4}: {'>' if result2 else '<'}")
    
    num5 = 20
    num6 = 15
    result3 = compare_numbers(num5, num6)
    print(f"Comparing {num5} and {num6}: {'>' if result3 else '<'}")