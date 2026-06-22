def reverse_integer(n):
    if n == 0:
        return 0
    negative = n < 0
    digits = []
    num = abs(n)
    while num > 0:
        digits.append(num % 10)
        num //= 10
    result = 0
    multiplier = 1
    for d in reversed(digits):
        result += d * multiplier
        multiplier *= 10
    if negative:
        result = -result
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(0))
    print(reverse_integer(9870))
    print(reverse_integer(-100))