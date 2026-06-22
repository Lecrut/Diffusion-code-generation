def int_to_binary(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append('1' if n & 1 else '0')
        n >>= 1
    return ''.join(reversed(bits))

if __name__ == '__main__':
    number = 42
    result = int_to_binary(number)
    print(result)
    number = 255
    result = int_to_binary(number)
    print(result)
    number = 0
    result = int_to_binary(number)
    print(result)