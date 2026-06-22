def binary_to_hex(bit_list):
    if not bit_list:
        return "0"
    
    value = 0
    for bit in bit_list:
        value = (value << 1) | bit
    
    if value == 0:
        return "0"
    
    hex_digits = "0123456789ABCDEF"
    result = []
    
    while value > 0:
        remainder = value & 0xF
        result.append(hex_digits[remainder])
        value = value >> 4
    
    return "".join(reversed(result))

if __name__ == '__main__':
    sample_bits = [1, 1, 0, 1, 1, 0, 1, 0]
    hex_result = binary_to_hex(sample_bits)
    print(hex_result)