def convert_hex_to_int_list(hex_strings):
    return [int(hex_str, 16) for hex_str in hex_strings]

if __name__ == '__main__':
    sample_hex_list = ['0xFF', '0x10', '0xAB', '0x1A3']
    result = convert_hex_to_int_list(sample_hex_list)
    print(result)