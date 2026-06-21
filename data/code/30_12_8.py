def decimal_to_binary(n: int) -> str:
    if n == 0:
        return '0'
    negative = n < 0
    n = abs(n)
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    result = ''.join(reversed(bits))
    return '-' + result if negative else result

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(5))
    print(decimal_to_binary(-5))
    print(decimal_to_binary(1024))
    print(decimal_to_binary(2**63 - 1))
    print(decimal_to_binary(123456789012345678901234567890))