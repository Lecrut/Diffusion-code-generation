def reverse_integer(n: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    negative = n < 0
    n_abs = abs(n)
    
    reversed_num = 0
    while n_abs > 0:
        digit = n_abs % 10
        n_abs //= 10
        
        if reversed_num > (INT_MAX - digit) // 10:
            return 0
        
        reversed_num = reversed_num * 10 + digit
    
    result = reversed_num if not negative else -reversed_num
    
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