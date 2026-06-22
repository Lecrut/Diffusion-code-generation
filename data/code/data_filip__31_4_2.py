def hex_strings_to_integers(hex_strings):
    return [int(hex_str, 16) for hex_str in hex_strings]

if __name__ == '__main__':
    sample_hex_strings = ['0x1a', '0xFF', '0x0', '0xdeadbeef']
    print(hex_strings_to_integers(sample_hex_strings))