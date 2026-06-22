def hex_to_decimal(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    hex_values = ["10", "FF", "deadBEEF", "0"]
    for hex_val in hex_values:
        print(hex_to_decimal(hex_val))