def hex_strings_to_ints(hex_strings):
    return [int(h, 16) for h in hex_strings]

if __name__ == '__main__':
    sample_hex = ['0x1A', '0xFF', '0x0', '0xDEADBEEF', '0x7F']
    print(hex_strings_to_ints(sample_hex))