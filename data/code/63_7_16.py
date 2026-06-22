def reverse_integer(n):
    if n == 0:
        return 0
    
    negative = n < 0
    n = abs(n)
    
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    
    return -reversed_num if negative else reversed_num

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(-6789))
    print(reverse_integer(1000))
    print(reverse_integer(0))