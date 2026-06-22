def reverse_digits(n: int) -> int:
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    
    result = sign * reversed_n
    
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    if result < INT_MIN or result > INT_MAX:
        return 0
    
    return result

if __name__ == '__main__':
    print(reverse_digits(123))
    print(reverse_digits(-456))
    print(reverse_digits(120))