def hex_to_decimal(hex_str):
    return int(hex_str, 16)

if __name__ == '__main__':
    hex_code = "1A3F"
    result = hex_to_decimal(hex_code)
    print(result)