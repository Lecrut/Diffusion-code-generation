def binary_to_hex(binary_str):
    if not binary_str:
        return ''
    num = 0
    for bit in binary_str:
        if bit not in ('0', '1'):
            raise ValueError("Invalid binary string")
        num = (num << 1) | (bit == '1')
    hex_str = format(num, 'x')
    return hex_str.upper()

if __name__ == '__main__':
    print(binary_to_hex('00001010'))
    print(binary_to_hex('11110000'))
    print(binary_to_hex('10101010'))
    print(binary_to_hex('00000001'))
    print(binary_to_hex('11111111'))
    print(binary_to_hex(''))