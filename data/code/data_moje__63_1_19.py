def reverse_integer(n):
    negative = n < 0
    num = abs(n)
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    if negative:
        reversed_num = -reversed_num
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(-6789))
    print(reverse_integer(1200))
    print(reverse_integer(0))
    print(reverse_integer(1))