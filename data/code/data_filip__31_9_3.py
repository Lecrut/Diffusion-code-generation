def hex_to_int(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    result = hex_to_int("1A3F")
    print(result)