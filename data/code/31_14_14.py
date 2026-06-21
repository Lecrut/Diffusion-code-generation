def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    result = 0
    hex_digits = '0123456789abcdefABCDEF'
    value_map = {}
    for i, digit in enumerate(hex_digits):
        if digit.isdigit():
            value_map[digit] = int(digit)
        else:
            value_map[digit] = 10 + (i - 10) if digit.islower() else 10 + (i - 10)
    for char in hex_string:
        result = result * 16 + value_map[char]
    return result

if __name__ == '__main__':
    sample_values = ['0', '1', 'A', 'FF', '1A3', '0x1A3', '10', 'DEADBEEF', '0xFFFFFFFF']
    for hex_val in sample_values:
        print(hex_to_decimal(hex_val))