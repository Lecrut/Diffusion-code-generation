def multiply_large_integers(a, b):
    if not all(char.isdigit() for char in a) or not all(char.isdigit() for char in b):
        raise ValueError("Both inputs must be strings representing non-negative integers.")
    
    result = 0
    len_a = len(a)
    len_b = len(b)
    
    for i in range(len_a - 1, -1, -1):
        digit_a = int(a[i])
        carry = 0
        temp_result = 0
        
        for j in range(len_b - 1, -1, -1):
            digit_b = int(b[j])
            product = (digit_a * digit_b) + carry
            temp_result += product * (10 ** (len_b - 1 - j))
            carry = product // 10
        
        result += temp_result * (10 ** i)
    
    return str(result)

if __name__ == '__main__':
    num1 = '987654321'
    num2 = '123456789'
    print(multiply_large_integers(num1, num2))