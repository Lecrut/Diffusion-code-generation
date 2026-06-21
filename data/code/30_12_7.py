def decimal_to_binary(n):
    if n == 0:
        return '0'
    is_negative = n < 0
    n = abs(n)
    bits = []
    while n > 0:
        bits.append('1' if n % 2 else '0')
        n //= 2
    result = ''.join(reversed(bits))
    if is_negative:
        result = '-' + result
    return result

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(-5))
    print(decimal_to_binary(0))
    print(decimal_to_binary(255))
    print(decimal_to_binary(1024))