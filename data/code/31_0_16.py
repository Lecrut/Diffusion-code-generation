def hex_to_decimal(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_hex_values = ["1A", "FF", "0", "100", "DEADBEEF"]
    for hex_val in sample_hex_values:
        decimal_result = hex_to_decimal(hex_val)
        print(decimal_result)