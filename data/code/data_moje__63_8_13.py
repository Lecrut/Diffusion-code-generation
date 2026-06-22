def reverse_integer(x: int) -> int:
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    reversed_num = 0
    
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    
    if reversed_num > INT_MAX:
        return 0
    
    return sign * reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1534236469))
    print(reverse_integer(2147483647))
    print(reverse_integer(-2147483648))