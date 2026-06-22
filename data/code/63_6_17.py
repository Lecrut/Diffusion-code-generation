def reverse_integer(n: int) -> int:
    sign = 1 if n >= 0 else -1
    reversed_digits = int(str(abs(n))[::-1])
    result = sign * reversed_digits
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if result < INT_MIN or result > INT_MAX:
        return 0
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(1534236469))