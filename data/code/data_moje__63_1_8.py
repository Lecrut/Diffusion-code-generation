def reverse_integer(n: int) -> int:
    negative = n < 0
    if negative:
        n = -n
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    if negative:
        reversed_n = -reversed_n
    return reversed_n

if __name__ == '__main__':
    print(reverse_integer(1234))
    print(reverse_integer(-6789))
    print(reverse_integer(1200))