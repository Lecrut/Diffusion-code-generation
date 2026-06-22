def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    result = 0
    for i, char in enumerate(reversed(hex_string)):
        char_lower = char.lower()
        if '0' <= char_lower <= '9':
            digit_value = ord(char_lower) - ord('0')
        elif 'a' <= char_lower <= 'f':
            digit_value = ord(char_lower) - ord('a') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        position = i
        weight = 16 ** position
        result += digit_value * weight
    return result

if __name__ == '__main__':
    sample_values = ['0', '1A', 'FF', '10', 'deadBEEF', '0x0', '0x1A']
    for sample in sample_values:
        print(hex_to_decimal(sample))