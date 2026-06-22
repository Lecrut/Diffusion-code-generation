def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    
    decimal_value = 0
    power = len(hex_string) - 1
    
    for char in hex_string:
        char = char.upper()
        if '0' <= char <= '9':
            digit_value = ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            digit_value = ord(char) - ord('A') + 10
        else:
            raise ValueError("Invalid hexadecimal digit: {}".format(char))
        decimal_value += digit_value * (16 ** power)
        power -= 1
    
    return decimal_value

if __name__ == '__main__':
    sample_hex_values = ['0', 'A', '1A', 'FF', '0x1a', 'DEADBEEF', '10']
    for hex_val in sample_hex_values:
        print(hex_to_decimal(hex_val))