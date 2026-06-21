def decimal_to_binary(n):
    if n == 0:
        return '0'
    stack = []
    if n < 0:
        n = -n
        prefix = '-'
    else:
        prefix = ''
    while n > 0:
        stack.append(n % 2)
        n = n // 2
    binary = ''.join(str(bit) for bit in reversed(stack))
    return prefix + binary

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(-42))
    print(decimal_to_binary(1))
    print(decimal_to_binary(1023))