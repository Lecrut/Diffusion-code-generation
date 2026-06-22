def reverse_integer(n):
    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)
    
    sign = -1 if n < 0 else 1
    n_abs = abs(n)
    
    reversed_num = 0
    while n_abs != 0:
        digit = n_abs % 10
        reversed_num = reversed_num * 10 + digit
        n_abs //= 10
    
    reversed_num *= sign
    
    if reversed_num < INT_MIN or reversed_num > INT_MAX:
        return 0
    
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))
    print(reverse_integer(-2147483648))