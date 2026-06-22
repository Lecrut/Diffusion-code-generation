def bin_to_hex(binary_str):
    if not binary_str:
        return '0'
    if not all(c in '01' for c in binary_str):
        raise ValueError("Input must be a binary string")
    value = 0
    for bit in binary_str:
        value = (value << 1) | int(bit)
    hex_digits = '0123456789ABCDEF'
    if value == 0:
        return '0'
    hex_str = ''
    while value > 0:
        remainder = value & 0xF
        hex_str = hex_digits[remainder] + hex_str
        value >>= 4
    return hex_str

if __name__ == '__main__':
    print(bin_to_hex('0'))
    print(bin_to_hex('1'))
    print(bin_to_hex('1010'))
    print(bin_to_hex('11110000'))
    print(bin_to_hex('00001010'))
    print(bin_to_hex('1111111111111111'))
    print(bin_to_hex('0000'))
    print(bin_to_hex('10'))
    print(bin_to_hex('11'))
    print(bin_to_hex('100'))