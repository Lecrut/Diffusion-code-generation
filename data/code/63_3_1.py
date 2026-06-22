def reverse_integer(x):
    sign = -1 if x < 0 else 1
    abs_x = abs(x)
    reversed_str = str(abs_x)[::-1]
    reversed_num = int(reversed_str)
    result = sign * reversed_num
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))