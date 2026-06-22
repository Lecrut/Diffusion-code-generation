def reverse_integer(n: int) -> int:
    negative = n < 0
    x = -n if negative else n
    result = 0
    while x > 0:
        result = result * 10 + x % 10
        x //= 10
    if negative:
        result = -result
    if result < -(2**31) or result > 2**31 - 1:
        return 0
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))