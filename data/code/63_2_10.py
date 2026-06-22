import math

def reverse_integer(n: int) -> int:
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    
    reversed_digits = 0
    original_n = n
    
    while n > 0:
        digit = n % 10
        reversed_digits = reversed_digits * 10 + digit
        n = n // 10
    
    result = sign * reversed_digits
    
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    if result < INT_MIN or result > INT_MAX:
        return 0
    
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))