def hex_to_decimal(hex_string):
    hex_string = hex_string.strip().upper()
    if hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    
    if not hex_string:
        return 0
    
    decimal_value = 0
    length = len(hex_string)
    
    for i, char in enumerate(hex_string):
        if char == 'X':
            continue
            
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        
        power = length - 1 - i
        decimal_value += digit * (16 ** power)
        
    return decimal_value

if __name__ == '__main__':
    samples = ["1A", "FF", "10", "0", "100"]
    for sample in samples:
        result = hex_to_decimal(sample)
        print(result)