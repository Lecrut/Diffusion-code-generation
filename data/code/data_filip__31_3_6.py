def hex_to_decimal(hex_string):
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        return int(hex_string, 16)
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_values = ['0x1A', '0xFF', '10', '0x42']
    for value in sample_values:
        print(hex_to_decimal(value))