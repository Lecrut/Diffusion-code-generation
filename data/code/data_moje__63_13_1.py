def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    abs_n = abs(n)
    reversed_abs = 0
    while abs_n > 0:
        digit = abs_n % 10
        reversed_abs = reversed_abs * 10 + digit
        abs_n //= 10
    result = sign * reversed_abs
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    if result < INT_MIN or result > INT_MAX:
        return 0
    return result
if __name__ == '__main__':
    sample_inputs = [123, -456, 120, 0, 1534236469]
    for value in sample_inputs:
        reversed_value = reverse_integer(value)
        print(reversed_value)