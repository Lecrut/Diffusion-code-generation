def decimal_to_binary(n: int) -> str:
    if n == 0:
        return '0'
    is_negative = n < 0
    n = abs(n)
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    binary_str = ''.join(reversed(bits))
    return f'-{binary_str}' if is_negative else binary_str

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(0))
    print(decimal_to_binary(-5))