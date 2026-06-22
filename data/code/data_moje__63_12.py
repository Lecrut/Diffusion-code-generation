def reverse_integer(n):
    if n == 0:
        return 0
    negative = n < 0
    n = abs(n)
    reversed_digits = []
    while n > 0:
        reversed_digits.append(n % 10)
        n //= 10
    reversed_number = int(''.join(map(str, reversed_digits)))
    if negative:
        reversed_number = -reversed_number
    return reversed_number

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(7890))
    print(reverse_integer(0))
    print(reverse_integer(5))
    print(reverse_integer(-100))