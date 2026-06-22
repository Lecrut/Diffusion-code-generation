def sum_digits(n):
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    
    return total

if __name__ == '__main__':
    num = 12345
    result = sum_digits(num)
    print(result)
    
    num2 = 0
    result2 = sum_digits(num2)
    print(result2)
    
    num3 = 999
    result3 = sum_digits(num3)
    print(result3)