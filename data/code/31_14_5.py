def hex_to_dec(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]
    if not hex_string:
        return 0
    
    value_map = {}
    for i in range(10):
        value_map[str(i)] = i
    for i in range(6):
        value_map[chr(ord('a') + i)] = 10 + i
        value_map[chr(ord('A') + i)] = 10 + i
    
    result = 0
    power = 1
    
    for char in reversed(hex_string):
        if char not in value_map:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        digit_value = value_map[char]
        result += digit_value * power
        power *= 16
    
    return result

if __name__ == '__main__':
    sample_inputs = ['1A', 'FF', '0', '10', 'ABCDEF', '0x10']
    for s in sample_inputs:
        print(hex_to_dec(s))