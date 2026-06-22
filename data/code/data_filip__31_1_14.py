def hex_to_decimal(hex_str):
    hex_str = hex_str.strip().lower()
    if hex_str.startswith('0x'):
        hex_str = hex_str[2:]
    if not hex_str:
        return 0
    
    decimal_value = 0
    length = len(hex_str)
    
    for i, char in enumerate(hex_str):
        pos = length - 1 - i
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit = ord(char) - ord('a') + 10
        else:
            raise ValueError(f"Invalid hex character: {char}")
        
        decimal_value += digit * (16 ** pos)
    
    return decimal_value

if __name__ == '__main__':
    result = hex_to_decimal('1A3F')
    print(result)