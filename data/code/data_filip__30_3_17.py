def int_to_binary_string(n):
    if n == 0:
        return '0'
    if n < 0:
        prefix = '-'
        n = -n
    else:
        prefix = ''
    
    bits = []
    while n > 0:
        if n & 1:
            bits.append('1')
        else:
            bits.append('0')
        n >>= 1
    
    return prefix + ''.join(reversed(bits))

if __name__ == '__main__':
    print(int_to_binary_string(0))
    print(int_to_binary_string(5))
    print(int_to_binary_string(255))
    print(int_to_binary_string(1024))
    print(int_to_binary_string(-12))
    print(int_to_binary_string(18446744073709551615))