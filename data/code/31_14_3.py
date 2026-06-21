def hex_to_decimal(hex_string):
    if not hex_string:
        return 0
    if hex_string.startswith('-'):
        return -hex_to_decimal(hex_string[1:])
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    result = 0
    for char in hex_string:
        if '0' <= char <= '9':
            value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            value = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            value = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal digit: {char}")
        result = result * 16 + value
    return result

if __name__ == '__main__':
    sample_values = [
        '0',
        '1a',
        'FF',
        'deadbeef',
        '0x1a',
        '0XFF',
        '-1a',
        '100'
    ]
    for sample in sample_values:
        print(hex_to_decimal(sample))