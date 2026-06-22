def reverse_integer(n):
    is_negative = n < 0
    n = abs(n)
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    if is_negative:
        return -reversed_num
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(-10))
    print(reverse_integer(1000))
    print(reverse_integer(-120))