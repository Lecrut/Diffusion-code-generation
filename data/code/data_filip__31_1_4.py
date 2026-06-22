def hex_to_decimal(hex_string: str) -> int:
    hex_string = hex_string.strip().lower()
    if hex_string.startswith('0x'):
        hex_string = hex_string[2:]
    
    if not hex_string:
        return 0
    
    value_map = {
        '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12,
        'd': 13, 'e': 14, 'f': 15
    }
    
    total = 0
    length = len(hex_string)
    
    for i in range(length):
        char = hex_string[i]
        if char not in value_map:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        
        digit_value = value_map[char]
        power = length - 1 - i
        total += digit_value * (16 ** power)
    
    return total

if __name__ == '__main__':
    test_cases = ["1A", "FF", "10", "ABCDEF", "0", "0x1F"]
    for test in test_cases:
        print(f"{test}: {hex_to_decimal(test)}")