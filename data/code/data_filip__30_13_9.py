def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    sign = ""
    if n < 0:
        sign = "-"
        n = -n
    binary_digits = []
    while n > 0:
        binary_digits.append('1' if n & 1 else '0')
        n >>= 1
    return sign + ''.join(reversed(binary_digits))

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(0))
    print(decimal_to_binary(-5))