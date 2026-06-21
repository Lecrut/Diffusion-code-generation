def decimal_to_binary(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    return ''.join(reversed(bits))

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(1))
    print(decimal_to_binary(5))
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(1024))
    print(decimal_to_binary(2**64 - 1))
    print(decimal_to_binary(10**18))