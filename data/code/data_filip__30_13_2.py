def decimal_to_binary(n):
    if n == 0:
        return '0'
    if n < 0:
        return '-' + decimal_to_binary(-n)
    bits = []
    while n:
        bits.append('1' if n & 1 else '0')
        n >>= 1
    return ''.join(reversed(bits))

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(5))
    print(decimal_to_binary(255))
    print(decimal_to_binary(-42))