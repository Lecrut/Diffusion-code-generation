def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        return int(hex_string, 16)
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_values = ['0xFF', '1A', '0x0', '7b']
    for val in sample_values:
        result = hex_to_decimal(val)
        print(f"{val} -> {result}")