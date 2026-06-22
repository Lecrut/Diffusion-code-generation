def hex_to_decimal(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_hex_values = ["FF", "1A3", "0", "10", "deadbeef"]
    for hex_val in sample_hex_values:
        result = hex_to_decimal(hex_val)
        print(result)