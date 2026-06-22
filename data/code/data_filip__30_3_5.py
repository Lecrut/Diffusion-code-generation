def int_to_binary_string(n: int) -> str:
    if n == 0:
        return "0"
    
    negative = n < 0
    value = n
    if negative:
        value = -n
    
    if value == 0:
        return "0"
    
    bits = []
    while value > 0:
        if value & 1:
            bits.append('1')
        else:
            bits.append('0')
        value >>= 1
    
    bits.reverse()
    result = ''.join(bits)
    
    if negative:
        result = '-' + result
        
    return result

if __name__ == '__main__':
    sample_values = [0, 1, 10, 255, 1024, -10, -255, 1000000]
    for val in sample_values:
        print(int_to_binary_string(val))