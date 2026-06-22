def reverse_integer(n):
    is_negative = n < 0
    if is_negative:
        n = -n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    if is_negative:
        reversed_num = -reversed_num
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if reversed_num > INT_MAX or reversed_num < INT_MIN:
        return 0
    return reversed_num

if __name__ == '__main__':
    samples = [123, -456, 120, 0]
    for val in samples:
        result = reverse_integer(val)
        print(result)