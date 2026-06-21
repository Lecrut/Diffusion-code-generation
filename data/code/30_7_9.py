def decimal_to_binary(n):
    if n == 0:
        return '0b0'
    if n == 1:
        return '0b1'
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    bits.reverse()
    return '0b' + ''.join(bits)

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(1))
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))