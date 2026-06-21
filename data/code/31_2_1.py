def hex_to_decimal(hex_str):
    hex_str = hex_str.strip()
    if hex_str.startswith(('0x', '0X')):
        hex_str = hex_str[2:]
    if not hex_str:
        return 0
    is_negative = False
    if hex_str.startswith('-'):
        is_negative = True
        hex_str = hex_str[1:]
    elif hex_str.startswith('+'):
        hex_str = hex_str[1:]
    
    hex_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    
    decimal_value = 0
    power = 0
    for char in reversed(hex_str):
        if char in hex_map:
            decimal_value += hex_map[char] * (16 ** power)
            power += 1
        else:
            raise ValueError(f"Invalid hex character: {char}")
    
    if is_negative:
        decimal_value = -decimal_value
    return decimal_value

if __name__ == '__main__':
    print(hex_to_decimal('0x1A'))
    print(hex_to_decimal('FF'))
    print(hex_to_decimal('0x10'))
    print(hex_to_decimal('-1F'))
    print(hex_to_decimal('0'))
    print(hex_to_decimal('deadBEEF'))