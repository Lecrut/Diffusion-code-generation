def hex_to_decimal(hex_str):
    return int(hex_str, 16)

if __name__ == '__main__':
    hex_values = ["1A", "FF", "100", "abc123"]
    for h in hex_values:
        print(hex_to_decimal(h))