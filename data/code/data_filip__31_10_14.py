def hex_to_decimal(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_hex = '1A3F'
    result = hex_to_decimal(sample_hex)
    print(result)
    sample_hex_2 = 'FF'
    print(hex_to_decimal(sample_hex_2))