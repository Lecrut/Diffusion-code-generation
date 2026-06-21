def hex_to_decimal(hex_str: str) -> int:
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        hex_str = hex_str[2:]
    result = 0
    for char in hex_str.upper():
        result <<= 4
        if '0' <= char <= '9':
            result |= ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            result |= ord(char) - ord('A') + 10
    return result
if __name__ == '__main__':
    sample_values = ['0x1A3', 'FF', '2F', '0x0', '10']
    for val in sample_values:
        print(f"hex_to_decimal('{val}') = {hex_to_decimal(val)}")