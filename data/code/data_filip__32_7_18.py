def binary_to_hex(binary_str):
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if len(binary_str) % 4 != 0:
        binary_str = binary_str.zfill(len(binary_str) + (4 - len(binary_str) % 4))
    
    nibbles = [binary_str[i:i+4] for i in range(0, len(binary_str), 4)]
    hex_digits = [hex_chars[int(nibble, 2)] for nibble in nibbles]
    
    return ''.join(hex_digits)

if __name__ == '__main__':
    result = binary_to_hex('1101011010')
    print(result)