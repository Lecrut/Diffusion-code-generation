def hex_string_to_int(hex_str: str) -> int:
    if not hex_str:
        return 0
    is_negative = False
    start_index = 0
    if hex_str.startswith('-'):
        is_negative = True
        start_index = 1
    if hex_str.startswith('0x', start_index) or hex_str.startswith('0X', start_index):
        start_index += 2
    
    result = 0
    digit_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    
    for char in hex_str[start_index:]:
        if char in digit_map:
            result = (result << 4) | digit_map[char]
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
    
    return -result if is_negative else result

if __name__ == '__main__':
    test_cases = ['FF', '1A', '0x1F', '-10', 'ABCDEF', 'cafe']
    for case in test_cases:
        print(hex_string_to_int(case))