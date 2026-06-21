def hex_to_decimal(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_hex_values = ['FF', '1A', 'deadbeef', '0']
    for value in sample_hex_values:
        print(hex_to_decimal(value))