def reverse_int(n):
    if n == 0:
        return 0
    
    negative = n < 0
    num = abs(n)
    result = 0
    
    while num > 0:
        digit = num % 10
        result = result * 10 + digit
        num //= 10
    
    if negative:
        return -result
    return result

if __name__ == '__main__':
    print(reverse_int(1234))
    print(reverse_int(-456))
    print(reverse_int(0))
    print(reverse_int(1200))