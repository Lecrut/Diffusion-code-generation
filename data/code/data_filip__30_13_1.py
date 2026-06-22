def int_to_binary(n):
    if n == 0:
        return '0'
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    bits = []
    while n > 0:
        bits.append('1' if n & 1 else '0')
        n >>= 1
    if is_negative:
        return '-' + ''.join(reversed(bits))
    return ''.join(reversed(bits))

if __name__ == '__main__':
    sample_value = 42
    print(int_to_binary(sample_value))
    print(int_to_binary(-15))
    print(int_to_binary(0))