def multiply_large_integers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative")
    
    result = 0
    for i in range(len(str(b))):
        digit_b = int(str(b)[len(str(b)) - 1 - i])
        carry = 0
        temp_result = 0
        for j in range(len(str(a))):
            digit_a = int(str(a)[len(str(a)) - 1 - j])
            product = (digit_a * digit_b) + carry
            temp_result += product * (10 ** j)
            carry = product // 10
        result += temp_result * (10 ** i)
    
    return result

if __name__ == '__main__':
    print(multiply_large_integers(123456789, 987654321))