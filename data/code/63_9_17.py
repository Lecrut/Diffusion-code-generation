def reverse_integer(n):
    if n == 0:
        return 0
    negative = n < 0
    n = abs(n)
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    if negative:
        reversed_n = -reversed_n
    return reversed_n

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1))
    print(reverse_integer(-100))