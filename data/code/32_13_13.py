def binary_to_hex(binary_str: str) -> str:
    if not binary_str:
        return ''
    
    padding_needed = (4 - len(binary_str) % 4) % 4
    binary_str = '0' * padding_needed + binary_str
    
    hex_digits = '0123456789abcdef'
    result = []
    
    for i in range(0, len(binary_str), 4):
        nibble = binary_str[i:i+4]
        decimal_val = int(nibble, 2)
        result.append(hex_digits[decimal_val])
    
    return ''.join(result)

if __name__ == '__main__':
    binary_input = "1111000010101010"
    hex_output = binary_to_hex(binary_input)
    print(hex_output)