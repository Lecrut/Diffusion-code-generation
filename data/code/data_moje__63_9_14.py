def reverse_integer(n):
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    
    reversed_digits = 0
    while n > 0:
        remainder = n % 10
        reversed_digits = reversed_digits * 10 + remainder
        n = n // 10
    
    return sign * reversed_digits

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(-6789))
    print(reverse_integer(0))
    print(reverse_integer(1000))
    print(reverse_integer(120))