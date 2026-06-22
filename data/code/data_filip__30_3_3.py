def int_to_binary_string(n: int) -> str:
    if n == 0:
        return '0'
    if n < 0:
        return '-' + int_to_binary_string(-n)
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    return ''.join(reversed(bits))

if __name__ == '__main__':
    sample_values = [0, 1, 2, 5, 10, 100, 255, 1024, 123456789012345678901234567890]
    for val in sample_values:
        print(int_to_binary_string(val))