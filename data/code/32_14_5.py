def binary_to_hex(binary_str):
    if not binary_str:
        return '0'
    
    decimal_value = int(binary_str, 2)
    
    if decimal_value == 0:
        return '0'
    
    hex_chars = '0123456789abcdef'
    result = []
    is_negative = decimal_value < 0
    if is_negative:
        decimal_value = -decimal_value
    
    while decimal_value > 0:
        remainder = decimal_value % 16
        result.append(hex_chars[remainder])
        decimal_value //= 16
    
    if is_negative:
        result.append('-')
    
    result.reverse()
    
    return ''.join(result)

if __name__ == '__main__':
    sample_binary = '1010101011110000'
    hex_result = binary_to_hex(sample_binary)
    print(hex_result)
    
    zero_binary = '0000'
    zero_hex = binary_to_hex(zero_binary)
    print(zero_hex)
    
    negative_binary = '-10101010'
    neg_hex = binary_to_hex(negative_binary)
    print(neg_hex)