def reverse_integer(n):
    negative = n < 0
    num = abs(n)
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    if negative:
        reversed_num = -reversed_num
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    if reversed_num < INT_MIN or reversed_num > INT_MAX:
        return 0
    return reversed_num
if __name__ == '__main__':
    sample_values = [123, -456, 120, 0, 1534236469]
    for val in sample_values:
        result = reverse_integer(val)
        print(result)