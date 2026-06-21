def hex_to_decimal(hex_str):
    hex_str = hex_str.strip()
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        hex_str = hex_str[2:]
    
    result = 0
    hex_chars = '0123456789abcdefABCDEF'
    
    for char in hex_str:
        if char not in hex_chars:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        if '0' <= char <= '9':
            value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            value = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            value = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        result = result * 16 + value
    
    return result

if __name__ == '__main__':
    test_cases = [
        "0x1A",
        "ff",
        "FF",
        "0",
        "10",
        "deadBEEF",
        "A",
        "a",
        "0x0",
        "123"
    ]
    for hex_code in test_cases:
        result = hex_to_decimal(hex_code)
        expected = int(hex_code, 16) if not hex_code.lower().startswith('0x') else int(hex_code, 16)
        if hex_code.lower().startswith('0x'):
            expected = int(hex_code, 16)
        print(f"hex: {hex_code}, decimal: {result}, expected: {expected}, match: {result == expected}")