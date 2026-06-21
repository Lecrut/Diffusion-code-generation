def hex_to_dec(hex_code):
    return int(hex_code, 16)

if __name__ == '__main__':
    result = hex_to_dec("1A3F")
    print(result)