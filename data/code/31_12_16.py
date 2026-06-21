def hex_list_to_decimal(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    sample_hex_values = [
        "0x1A", "0xFF", "0x0", "0x7FFFFFFF",
        "0x100", "0xDEADBEEF", "0xCAFE",
        "0x1", "0xABCDEF1234567890", "0x0000"
    ]
    result = hex_list_to_decimal(sample_hex_values)
    print(result)