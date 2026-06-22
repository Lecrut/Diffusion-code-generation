def convert_hex_batch(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    sample_hex = ['0x1A', '0xFF', '0x100', '0xDEAD', '0xBEEF']
    print(convert_hex_batch(sample_hex))