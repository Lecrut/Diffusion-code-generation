def reverse_integer(x):
    if x == 0:
        return 0
    negative = x < 0
    value = -x if negative else x
    reversed_value = 0
    while value > 0:
        digit = value % 10
        reversed_value = reversed_value * 10 + digit
        value //= 10
    if negative:
        reversed_value = -reversed_value
    return reversed_value

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))