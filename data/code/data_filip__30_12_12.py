def decimal_to_binary(n):
    if n == 0:
        return "0"
    is_negative = n < 0
    n = abs(n)
    result = []
    while n > 0:
        result.append(str(n & 1))
        n >>= 1
    binary_str = "".join(reversed(result))
    return "-" + binary_str if is_negative else binary_str

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(12345678901234567890))
    print(decimal_to_binary(-42))
    print(decimal_to_binary(2**1000))