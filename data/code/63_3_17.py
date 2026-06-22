def reverse_integer(n):
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    if n == 0:
        return 0
    
    sign = 1 if n > 0 else -1
    n_abs = abs(n)
    
    reversed_n = 0
    while n_abs > 0:
        digit = n_abs % 10
        reversed_n = reversed_n * 10 + digit
        n_abs = n_abs // 10
    
    result = sign * reversed_n
    
    if result < INT_MIN or result > INT_MAX:
        return 0
    
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(2147483647))
    print(reverse_integer(-2147483648))
    print(reverse_integer(1534236469))