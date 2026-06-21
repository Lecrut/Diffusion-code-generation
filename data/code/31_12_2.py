def hex_list_to_decimal(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    sample_hexes = [
        "1A2B3C",
        "FF",
        "0",
        "DEADBEEF",
        "cafe",
        "1234567890ABCDEF"
    ]
    results = hex_list_to_decimal(sample_hexes)
    print(results)