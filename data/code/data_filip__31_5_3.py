def hex_to_decimal(hex_code):
    return int(hex_code, 16)

if __name__ == '__main__':
    result = hex_to_decimal("FF")
    print(result)