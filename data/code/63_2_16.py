def reverse_integer(x):
    sign = 1 if x >= 0 else -1
    abs_x = abs(x)
    reversed_str = str(abs_x)[::-1]
    reversed_int = int(reversed_str)
    result = sign * reversed_int
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result

if __name__ == '__main__':
    test_values = [123, -123, 120, 1534236469, 0]
    for val in test_values:
        print(reverse_integer(val))