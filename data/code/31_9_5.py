def hex_to_int(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_hex = "1A3F"
    result = hex_to_int(sample_hex)
    print(result)