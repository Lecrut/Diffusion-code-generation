def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if not hex_string:
        return 0
    
    is_negative = False
    if hex_string.startswith('-'):
        is_negative = True
        hex_string = hex_string[1:]
    elif hex_string.startswith('+'):
        hex_string = hex_string[1:]
    
    if not hex_string:
        return 0
    
    digit_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    
    total_value = 0
    power = 0
    index = len(hex_string) - 1
    
    while index >= 0:
        char = hex_string[index]
        if char not in digit_map:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        digit_value = digit_map[char]
        total_value += digit_value * (16 ** power)
        power += 1
        index -= 1
    
    if is_negative:
        return -total_value
    return total_value

if __name__ == '__main__':
    sample_hex_1 = "1A3F"
    sample_hex_2 = "deadbeef"
    sample_hex_3 = "-2B"
    
    result_1 = hex_to_decimal(sample_hex_1)
    result_2 = hex_to_decimal(sample_hex_2)
    result_3 = hex_to_decimal(sample_hex_3)
    
    print(result_1)
    print(result_2)
    print(result_3)