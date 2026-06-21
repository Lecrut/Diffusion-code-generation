def hex_to_decimal(hex_str):
    hex_str = hex_str.strip().upper()
    if not hex_str:
        return 0
    
    decimal_value = 0
    length = len(hex_str)
    
    for i, char in enumerate(hex_str):
        if char in '0123456789':
            digit = ord(char) - ord('0')
        elif char in 'ABCDEF':
            digit = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        
        power = length - 1 - i
        decimal_value += digit * (16 ** power)
        
    return decimal_value

if __name__ == '__main__':
    sample_hex = "1A3F"
    result = hex_to_decimal(sample_hex)
    print(result)