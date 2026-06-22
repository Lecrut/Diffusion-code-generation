def reverse_integer(n: int) -> int:
    if n == 0:
        return 0
    
    negative = n < 0
    num = -n if negative else n
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    return -reversed_num if negative else reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1200))