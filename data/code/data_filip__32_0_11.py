def binary_to_hex(binary_str):
    hex_chars = '0123456789abcdef'
    if not binary_str:
        return '0'
    remainder = len(binary_str) % 4
    if remainder != 0:
        binary_str = '0' * (4 - remainder) + binary_str
    hex_digits = []
    for i in range(0, len(binary_str), 4):
        chunk = binary_str[i:i + 4]
        value = 0
        for bit in chunk:
            value = (value << 1) + int(bit)
        hex_digits.append(hex_chars[value])
    hex_result = ''.join(hex_digits)
    hex_result = hex_result.lstrip('0')
    if not hex_result:
        return '0'
    return hex_result
if __name__ == '__main__':
    print(binary_to_hex('1101'))
    print(binary_to_hex('10101010'))
    print(binary_to_hex('11111111'))
    print(binary_to_hex('0'))
    print(binary_to_hex('1'))
    print(binary_to_hex('1000000000000000'))