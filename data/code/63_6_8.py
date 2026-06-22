def reverse_integer(n: int) -> int:
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    
    reversed_num *= sign
    
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    if reversed_num > INT_MAX or reversed_num < INT_MIN:
        return 0
    
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(1534236469))