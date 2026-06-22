def reverse_integer(n: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    sign = 1 if n >= 0 else -1
    abs_n = abs(n)
    
    reversed_n = 0
    while abs_n > 0:
        digit = abs_n % 10
        reversed_n = reversed_n * 10 + digit
        abs_n = abs_n // 10
    
    reversed_n = sign * reversed_n
    
    if reversed_n > INT_MAX or reversed_n < INT_MIN:
        return 0
    
    return reversed_n

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(1534236469))
    print(reverse_integer(0))