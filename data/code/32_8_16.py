def binary_to_hex(binary_string):
    if not binary_string:
        return "0"
    return hex(int(binary_string, 2))[2:]

if __name__ == '__main__':
    print(binary_to_hex("1010"))
    print(binary_to_hex("0000"))
    print(binary_to_hex("11111111"))
    print(binary_to_hex(""))
    print(binary_to_hex("00010101"))