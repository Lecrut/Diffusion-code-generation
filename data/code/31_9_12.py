def hex_to_int(hex_str):
    return int(hex_str, 16)

if __name__ == '__main__':
    result = hex_to_int('1A3F')
    print(result)