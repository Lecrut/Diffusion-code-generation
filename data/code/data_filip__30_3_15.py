def int_to_binary(n: int) -> str:
    if n == 0:
        return '0'
    is_negative = n < 0
    if is_negative:
        n = -n
    bits = []
    while n > 0:
        bits.append('1' if n & 1 else '0')
        n >>= 1
    if is_negative:
        bits.append('-')
    bits.reverse()
    return ''.join(bits)

if __name__ == '__main__':
    large_positive = 123456789012345678901234567890
    large_negative = -987654321098765432109876543210
    print(int_to_binary(large_positive))
    print(int_to_binary(large_negative))