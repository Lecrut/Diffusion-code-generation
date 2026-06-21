def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith("0x") or hex_string.startswith("0X"):
        hex_string = hex_string[2:]
    if not hex_string:
        raise ValueError("Empty hexadecimal string")
    
    result = 0
    length = len(hex_string)
    
    for index, char in enumerate(hex_string):
        position = length - 1 - index
        
        if '0' <= char <= '9':
            digit_value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit_value = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            digit_value = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        
        result += digit_value * (16 ** position)
    
    return result

if __name__ == '__main__':
    print(hex_to_decimal("1A3"))
    print(hex_to_decimal("0xFF"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("deadbeef"))
    print(hex_to_decimal("A"))
    print(hex_to_decimal("10"))