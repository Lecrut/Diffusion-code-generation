def binary_to_hex(binary_string):
    if not binary_string:
        return '0'
    decimal_value = int(binary_string, 2)
    hex_value = hex(decimal_value)[2:].upper()
    return hex_value

if __name__ == '__main__':
    print(binary_to_hex('1010'))
    print(binary_to_hex('0000'))
    print(binary_to_hex('11111111'))
    print(binary_to_hex('0'))
    print(binary_to_hex('1'))
    print(binary_to_hex('00001010'))
    print(binary_to_hex('100000000'))