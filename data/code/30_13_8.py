def decimal_to_binary(n: int = 42) -> str:
    if n == 0:
        return '0'
    is_negative = n < 0
    n = abs(n)
    bits = []
    while n > 0:
        bits.append('1' if n & 1 else '0')
        n >>= 1
    binary_str = ''.join(reversed(bits))
    if is_negative:
        binary_str = '-' + binary_str
    return binary_str

if __name__ == '__main__':
    print(decimal_to_binary(42))
    print(decimal_to_binary(-10))
    print(decimal_to_binary(0))
    print(decimal_to_binary(1))