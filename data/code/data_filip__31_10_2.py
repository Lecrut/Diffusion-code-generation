def hex_to_decimal(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_hex = "1A3F"
    print(hex_to_decimal(sample_hex))