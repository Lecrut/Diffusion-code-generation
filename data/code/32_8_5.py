def binary_to_hex(binary_string):
    if not binary_string:
        return '0'
    stripped = binary_string.lstrip('0')
    if not stripped:
        return '0'
    return hex(int(stripped, 2))[2:].upper()

if __name__ == '__main__':
    print(binary_to_hex('1010'))
    print(binary_to_hex('00001010'))
    print(binary_to_hex('0000'))
    print(binary_to_hex(''))
    print(binary_to_hex('11111111'))