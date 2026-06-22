def reverse_integer(n: int) -> int:
    is_negative = n < 0
    s = str(n)
    if is_negative:
        reversed_s = "-" + s[1:][::-1]
    else:
        reversed_s = s[::-1]
    result = int(reversed_s)
    if not (-2**31 <= result <= 2**31 - 1):
        return 0
    return result

if __name__ == '__main__':
    test_cases = [123, -456, 120, 0, -10, 1534236469, -2147483648]
    for val in test_cases:
        print(reverse_integer(val))