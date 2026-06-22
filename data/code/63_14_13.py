def reverse_integer(n):
    sign = -1 if n < 0 else 1
    reversed_str = "".join([digit for digit in str(abs(n))[::-1]])
    return sign * int(reversed_str)

if __name__ == '__main__':
    result = reverse_integer(12345)
    print(result)
    result = reverse_integer(-6789)
    print(result)
    result = reverse_integer(1200)
    print(result)