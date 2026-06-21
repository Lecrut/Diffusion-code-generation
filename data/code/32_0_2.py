def binary_to_hexadecimal(binary_string):
    if not binary_string:
        return '0'
    valid_chars = set('01')
    for char in binary_string:
        if char not in valid_chars:
            raise ValueError('Invalid binary string')
    hex_map = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    padding_length = 4 - len(binary_string) % 4
    if padding_length != 4:
        padded_binary = '0' * padding_length + binary_string
    else:
        padded_binary = binary_string
    hexadecimal = []
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i:i + 4]
        hex_digit = hex_map[chunk]
        hexadecimal.append(hex_digit)
    result = ''.join(hexadecimal)
    result = result.lstrip('0')
    if not result:
        return '0'
    return result
if __name__ == '__main__':
    print(binary_to_hexadecimal('101010'))
    print(binary_to_hexadecimal('1111'))
    print(binary_to_hexadecimal('0'))
    print(binary_to_hexadecimal('100111101011'))