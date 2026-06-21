def hex_to_decimal(hex_str):
    hex_str = hex_str.strip()
    if not hex_str:
        return 0
    
    negative = False
    if hex_str.startswith('-'):
        negative = True
        hex_str = hex_str[1:]
    
    valid_chars = set('0123456789abcdefABCDEF')
    if not all(c in valid_chars for c in hex_str):
        raise ValueError("Invalid hexadecimal character")
    
    hex_str = hex_str.lower()
    decimal_value = 0
    length = len(hex_str)
    
    for i, char in enumerate(hex_str):
        if char in '0123456789':
            digit = ord(char) - ord('0')
        else:
            digit = ord(char) - ord('a') + 10
        
        position_from_right = length - 1 - i
        decimal_value += digit * (16 ** position_from_right)
    
    if negative:
        decimal_value = -decimal_value
        
    return decimal_value

if __name__ == '__main__':
    samples = ["1A", "FF", "100", "-1F", "0", "0123456789ABCDEF"]
    for s in samples:
        result = hex_to_decimal(s)
        print(result)