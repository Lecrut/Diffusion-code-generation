def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n_abs = abs(n)
    reversed_str = str(n_abs)[::-1]
    reversed_int = int(reversed_str)
    result = sign * reversed_int
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result

if __name__ == '__main__':
    sample_values = [123, -456, 0, 1534236469, 2147483647, -2147483648]
    for val in sample_values:
        print(reverse_integer(val))