def decimal_to_binary(n):
    if n == 0:
        return '0'
    result = []
    while n > 0:
        result.append(str(n & 1))
        n >>= 1
    return ''.join(reversed(result))

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(0))
    print(decimal_to_binary(1))