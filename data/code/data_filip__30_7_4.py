def decimal_to_binary(n):
    if n == 0:
        return '0b0'
    if n == 1:
        return '0b1'
    
    bits = []
    is_negative = n < 0
    n = abs(n)
    
    while n > 0:
        bits.append(str(n % 2))
        n = n // 2
    
    binary_str = ''.join(reversed(bits))
    
    if is_negative:
        return '-0b' + binary_str
    else:
        return '0b' + binary_str

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(1))
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(-7))
    print(decimal_to_binary(1024))