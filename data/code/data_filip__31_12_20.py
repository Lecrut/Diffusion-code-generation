def hex_to_decimal(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    sample_hex = ['1A', 'FF', '0', '2F', '100', 'ABCDEF']
    results = hex_to_decimal(sample_hex)
    print(results)