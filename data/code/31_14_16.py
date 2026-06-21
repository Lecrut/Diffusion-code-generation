def hex_to_decimal(hex_string):
    hex_string = hex_string.strip().lstrip('0x').lstrip('0X')
    if not hex_string:
        return 0
    digit_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    result = 0
    multiplier = 1
    for char in reversed(hex_string):
        if char not in digit_map:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        result += digit_map[char] * multiplier
        multiplier *= 16
    return result

if __name__ == '__main__':
    sample_hex = "1A3F"
    print(hex_to_decimal(sample_hex))
    sample_hex2 = "ff"
    print(hex_to_decimal(sample_hex2))
    sample_hex3 = "0"
    print(hex_to_decimal(sample_hex3))
    sample_hex4 = "deadbeef"
    print(hex_to_decimal(sample_hex4))