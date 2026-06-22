def reverse_integer(n: int) -> int:
    sign = 1 if n >= 0 else -1
    abs_n = abs(n)
    reversed_str = str(abs_n)[::-1]
    reversed_val = int(reversed_str)
    result = sign * reversed_val
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(1534236469))