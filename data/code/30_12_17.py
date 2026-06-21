def decimal_to_binary(n):
    if n == 0:
        return '0'
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    binary_str = ''.join(reversed(bits))
    if is_negative:
        return '-' + binary_str
    return binary_str
if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(1024))
    print(decimal_to_binary(-10))
    print(decimal_to_binary(10 ** 100))