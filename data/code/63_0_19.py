def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    num = abs(n)
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    reversed_num *= sign
    
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))