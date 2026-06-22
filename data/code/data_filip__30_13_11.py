def decimal_to_binary(n):
    if n == 0:
        return '0'
    negative = n < 0
    n = abs(n)
    bits = []
    while n:
        bits.append('1' if n & 1 else '0')
        n >>= 1
    result = ''.join(reversed(bits))
    return '-' + result if negative else result

if __name__ == '__main__':
    print(decimal_to_binary(42))
    print(decimal_to_binary(0))
    print(decimal_to_binary(-13))
    print(decimal_to_binary(255))