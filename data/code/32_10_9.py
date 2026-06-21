def binary_to_hex(binary_str):
    if not binary_str:
        return "0"
    
    hex_chars = '0123456789abcdef'
    hex_result = []
    
    padded_len = (len(binary_str) + 3) // 4 * 4
    binary_str = binary_str.zfill(padded_len)
    
    for i in range(0, len(binary_str), 4):
        chunk = binary_str[i:i+4]
        value = 0
        for bit in chunk:
            value = (value << 1) | int(bit)
        hex_result.append(hex_chars[value])
    
    return ''.join(hex_result).lstrip('0') or '0'

if __name__ == '__main__':
    print(binary_to_hex('1010'))
    print(binary_to_hex('00001010'))
    print(binary_to_hex('111111111111'))
    print(binary_to_hex('0'))