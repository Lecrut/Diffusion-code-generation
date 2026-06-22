def reverse_integer(n):
    sign = -1 if n < 0 else 1
    x = abs(n)
    reversed_x = 0
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    
    while x != 0:
        digit = x % 10
        x = x // 10
        
        if reversed_x > (INT_MAX - digit) // 10:
            return 0
        
        reversed_x = reversed_x * 10 + digit
    
    result = sign * reversed_x
    
    if result < INT_MIN or result > INT_MAX:
        return 0
    
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(1534236469))
    print(reverse_integer(0))