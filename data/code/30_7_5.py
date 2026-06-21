def decimal_to_binary(n):
    if n == 0:
        return '0b0'
    if n == 1:
        return '0b1'
    
    is_negative = n < 0
    n = abs(n)
    
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    
    bits.reverse()
    result = ''.join(bits)
    
    if is_negative:
        result = '-' + result
    
    return '0b' + result

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(1))
    print(decimal_to_binary(10))
    print(decimal_to_binary(-5))
    print(decimal_to_binary(255))