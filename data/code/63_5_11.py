def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    n_abs = abs(n)
    reversed_num = 0
    while n_abs > 0:
        reversed_num = reversed_num * 10 + n_abs % 10
        n_abs //= 10
    result = sign * reversed_num
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    if result < INT_MIN or result > INT_MAX:
        return 0
    return result
if __name__ == '__main__':
    sample_values = [123, -456, 120, 0, 1534236469, -2147483648]
    for n in sample_values:
        result = reverse_integer(n)
        print(result)