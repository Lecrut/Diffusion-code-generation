def hex_to_decimal_batch(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    sample_hex_values = [
        "0x1A",
        "0xFF",
        "0x0",
        "0x123ABC",
        "0xDEAD",
        "0xBEEF",
        "0xCAFEBABE",
        "0x10",
        "0xFFFFFFFF",
        "0x7FFFFFFF"
    ]
    print(hex_to_decimal_batch(sample_hex_values))