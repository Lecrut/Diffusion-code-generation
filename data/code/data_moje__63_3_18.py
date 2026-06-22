def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = 0
    while x:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10
    reversed_x *= sign
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    return reversed_x

if __name__ == '__main__':
    samples = [123, -456, 120, 0, 1534236469]
    for s in samples:
        print(reverse_integer(s))