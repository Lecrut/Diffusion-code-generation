def hex_to_decimal(hex_str):
    hex_str = hex_str.strip()
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        hex_str = hex_str[2:]
    if not hex_str:
        raise ValueError('Empty hex string')
    decimal_value = 0
    for char in hex_str:
        decimal_value *= 16
        if '0' <= char <= '9':
            decimal_value += ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            decimal_value += ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            decimal_value += ord(char) - ord('A') + 10
        else:
            raise ValueError(f'Invalid hex character: {char}')
    return decimal_value
if __name__ == '__main__':
    test_cases = [('0', 0), ('1', 1), ('A', 10), ('a', 10), ('F', 15), ('f', 15), ('10', 16), ('FF', 255), ('ff', 255), ('1A3', 419), ('1a3', 419), ('0x10', 16), ('0XFF', 255), ('0x0', 0), ('7F', 127), ('80', 128), ('100', 256), ('FFF', 4095), ('FFFF', 65535), ('10000', 65536)]
    for hex_input, expected in test_cases:
        result = hex_to_decimal(hex_input)
        print(f"hex_to_decimal('{hex_input}') = {result}, expected = {expected}, match = {result == expected}")