def hex_to_decimal(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    hex_values = ['0A', '1FF', 'DEADBEEF']
    for hex_val in hex_values:
        result = hex_to_decimal(hex_val)
        print(result)