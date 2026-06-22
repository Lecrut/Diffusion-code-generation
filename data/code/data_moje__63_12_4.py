def reverse_integer(x):
    if x == 0:
        return 0
    negative = x < 0
    digits = []
    abs_x = -x if negative else x
    while abs_x > 0:
        digits.append(abs_x % 10)
        abs_x //= 10
    result = 0
    for digit in digits:
        result = result * 10 + digit
    if negative:
        result = -result
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1200))
    print(reverse_integer(0))
    print(reverse_integer(-980))