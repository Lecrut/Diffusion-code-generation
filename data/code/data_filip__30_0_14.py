def int_to_binary(n):
    if n == 0:
        return '0'
    result = []
    while n > 0:
        result.append('0' if n % 2 == 0 else '1')
        n //= 2
    return ''.join(reversed(result))

if __name__ == '__main__':
    print(int_to_binary(0))
    print(int_to_binary(1))
    print(int_to_binary(2))
    print(int_to_binary(5))
    print(int_to_binary(10))
    print(int_to_binary(255))
    print(int_to_binary(1024))