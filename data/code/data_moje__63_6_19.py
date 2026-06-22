def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n_abs = abs(n)
    reversed_digits = int(str(n_abs)[::-1])
    result = sign * reversed_digits
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result

if __name__ == '__main__':
    test_values = [123, -123, 1534236469, 0, 120, -42]
    for value in test_values:
        print(reverse_integer(value))