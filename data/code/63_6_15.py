def reverse_integer(n: int) -> int:
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    sign = -1 if n < 0 else 1
    num = abs(n)
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num //= 10
    reversed_num *= sign
    if reversed_num > INT_MAX or reversed_num < INT_MIN:
        return 0
    return reversed_num
if __name__ == '__main__':
    sample_values = [123, -456, 120, 1534236469, -2147483648, 2147483647]
    for val in sample_values:
        result = reverse_integer(val)
        print(f'reverse_integer({val}) = {result}')