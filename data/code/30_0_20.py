def int_to_binary(n):
    if n == 0:
        return '0'
    result = []
    while n > 0:
        result.append('1' if n & 1 else '0')
        n >>= 1
    return ''.join(reversed(result))

if __name__ == '__main__':
    test_values = [0, 1, 2, 5, 10, 15, 16, 255, 1024, 65535]
    for value in test_values:
        print(f'{value}: {int_to_binary(value)}')