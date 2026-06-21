def hex_to_int(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_hex_values = [
        "1A3F",
        "FF",
        "0",
        "deadBEEF",
        "10"
    ]
    for hex_val in sample_hex_values:
        print(hex_to_int(hex_val))