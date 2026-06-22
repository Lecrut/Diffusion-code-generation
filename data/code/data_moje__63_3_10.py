def reverse_integer(n: int) -> int:
    INT_MIN = -2 ** 31
    INT_MAX = 2 ** 31 - 1
    sign = -1 if n < 0 else 1
    abs_n = abs(n)
    reversed_str = str(abs_n)[::-1]
    reversed_num = int(reversed_str)
    result = sign * reversed_num
    if result < INT_MIN or result > INT_MAX:
        return 0
    return result
if __name__ == '__main__':
    sample_values = [123, -456, 120, 1534236469, 0]
    for val in sample_values:
        print(reverse_integer(val))