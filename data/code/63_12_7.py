def reverse_integer(x):
    if x == 0:
        return 0
    negative = x < 0
    digits = []
    n = -x if negative else x
    while n > 0:
        digits.append(n % 10)
        n //= 10
    result = 0
    for i, d in enumerate(digits):
        result += d * (10 ** i)
    if negative:
        result = -result
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(700))
    print(reverse_integer(0))