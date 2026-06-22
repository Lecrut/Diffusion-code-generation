def reverse_integer(n):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    reversed_num = 0
    negative = n < 0
    num = abs(n)
    
    while num != 0:
        digit = num % 10
        num = num // 10
        
        if reversed_num > (INT_MAX - digit) // 10:
            return 0
        
        reversed_num = reversed_num * 10 + digit
    
    if negative:
        if reversed_num > (INT_MIN * -1):
            return 0
        reversed_num = -reversed_num
    else:
        if reversed_num > INT_MAX:
            return 0
    
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(2147483647))
    print(reverse_integer(-2147483648))
    print(reverse_integer(1534236469))
    print(reverse_integer(-1563847412))