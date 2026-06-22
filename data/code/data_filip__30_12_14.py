def decimal_to_binary(n):
    if n == 0:
        return '0'
    if n < 0:
        return '-' + decimal_to_binary(-n)
    result = []
    while n > 0:
        result.append('1' if n % 2 else '0')
        n >>= 1
    return ''.join(reversed(result))

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(5))
    print(decimal_to_binary(255))
    print(decimal_to_binary(1024))
    print(decimal_to_binary(-42))
    print(decimal_to_binary(123456789012345678901234567890))