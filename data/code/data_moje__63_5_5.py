def reverse_integer(n):
    sign = 1 if n >= 0 else -1
    abs_n = abs(n)
    reversed_num = 0
    while abs_n > 0:
        digit = abs_n % 10
        reversed_num = reversed_num * 10 + digit
        abs_n //= 10
    
    result = sign * reversed_num
    
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    if result < INT_MIN or result > INT_MAX:
        return 0
    
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))