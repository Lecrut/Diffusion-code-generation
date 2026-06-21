def hex_strings_to_integers(hex_list):
    return [int(hex_str, 16) for hex_str in hex_list]

if __name__ == '__main__':
    sample_hex_list = ['0x1A', '0xFF', '0x0', '0x10']
    result = hex_strings_to_integers(sample_hex_list)
    print(result)