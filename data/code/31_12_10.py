def hex_batch_to_decimal(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    sample_hex_values = ['0x1A', '0xFF', '0x1000', '0xDEADBEEF', '0xCAFEBABE']
    result = hex_batch_to_decimal(sample_hex_values)
    print(result)