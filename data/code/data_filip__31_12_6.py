def hex_to_decimal_batch(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    sample_hex = ["0xFF", "0x1A3", "0x0", "0xDEADBEEF", "0x123456789ABCDEF", "0xCAFE", "0xBABE"]
    print(hex_to_decimal_batch(sample_hex))