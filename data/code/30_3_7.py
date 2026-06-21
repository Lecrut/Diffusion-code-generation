def large_int_to_binary(n):
    if n == 0:
        return '0'
    if n < 0:
        return '-' + large_int_to_binary(-n)
    
    bits = []
    while n > 0:
        bit = n & 1
        bits.append(str(bit))
        n >>= 1
    
    bits.reverse()
    return ''.join(bits)

if __name__ == '__main__':
    sample_values = [0, 1, 2, 7, 15, 128, 255, 1024, 123456789012345678901234567890, -42]
    
    for val in sample_values:
        result = large_int_to_binary(val)
        print(result)