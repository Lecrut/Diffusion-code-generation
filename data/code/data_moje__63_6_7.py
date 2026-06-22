def reverse_integer(x):
    if x == 0:
        return 0
    
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    reversed_abs = 0
    
    while x_abs > 0:
        digit = x_abs % 10
        reversed_abs = reversed_abs * 10 + digit
        x_abs //= 10
    
    result = sign * reversed_abs
    
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    if result < INT_MIN or result > INT_MAX:
        return 0
    
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1534236469))
    print(reverse_integer(0))