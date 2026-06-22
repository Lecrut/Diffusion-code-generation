def hex_to_decimal(hex_values):
    return [int(h, 16) for h in hex_values]

if __name__ == '__main__':
    hex_data = ["1A", "FF", "100", "ABCDEF", "0"]
    results = hex_to_decimal(hex_data)
    print(results)