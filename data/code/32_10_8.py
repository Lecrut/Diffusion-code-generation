def binary_to_hex(binary_str):
    if not binary_str:
        return '0'
    
    value = 0
    for char in binary_str:
        if char == '0':
            value = (value << 1) | 0
        elif char == '1':
            value = (value << 1) | 1
        else:
            raise ValueError("Invalid binary digit found")
    
    hex_chars = "0123456789abcdef"
    if value == 0:
        return '0'
    
    hex_str = []
    while value > 0:
        nibble = value & 0xF
        hex_str.append(hex_chars[nibble])
        value >>= 4
    
    return ''.join(reversed(hex_str))

if __name__ == '__main__':
    samples = ['0', '1', '1010', '1111', '00001010', '11010011', '00000000', '11111111', '00110011']
    for sample in samples:
        print(binary_to_hex(sample))