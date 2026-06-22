def reverse_integer(n: int) -> int:
    if n == 0:
        return 0
    
    sign = -1 if n < 0 else 1
    num = abs(n)
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    
    return sign * reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1200))
    print(reverse_integer(0))
    print(reverse_integer(1))
    print(reverse_integer(1000000021))