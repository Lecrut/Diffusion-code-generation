def hex_to_dec(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]
    if not hex_string:
        return 0
    hex_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    result = 0
    power = 1
    for char in reversed(hex_string):
        if char not in hex_map:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        digit_value = hex_map[char]
        result += digit_value * power
        power *= 16
    return result

if __name__ == '__main__':
    sample_hex = "1A3F"
    print(hex_to_dec(sample_hex))
    sample_hex_neg = "-2B"
    print(hex_to_dec(sample_hex_neg[1:]) * (-1 if sample_hex_neg.startswith('-') else 1))
    sample_with_prefix = "0xFF"
    print(hex_to_dec(sample_with_prefix))