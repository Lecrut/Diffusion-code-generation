def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if not hex_string:
        return 0
    
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]
    
    if not hex_string:
        return 0
    
    digit_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    
    decimal_value = 0
    power = 1
    
    for i in range(len(hex_string) - 1, -1, -1):
        char = hex_string[i]
        if char not in digit_map:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        
        decimal_value += digit_map[char] * power
        power *= 16
        
    return decimal_value

if __name__ == '__main__':
    sample_hex_1 = "1A3F"
    sample_hex_2 = "0xFF"
    sample_hex_3 = "deadbeef"
    
    result_1 = hex_to_decimal(sample_hex_1)
    result_2 = hex_to_decimal(sample_hex_2)
    result_3 = hex_to_decimal(sample_hex_3)
    
    print(result_1)
    print(result_2)
    print(result_3)