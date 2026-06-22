def binary_to_hex(binary_string):
    if not binary_string:
        return '0'

    hex_map = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'a',
        '1011': 'b',
        '1100': 'c',
        '1101': 'd',
        '1110': 'e',
        '1111': 'f'
    }

    padding_length = 4 - len(binary_string) % 4
    if padding_length != 4:
        padded_binary = '0' * padding_length + binary_string
    else:
        padded_binary = binary_string

    hex_digits = []
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i:i + 4]
        hex_digits.append(hex_map[chunk])

    result = ''.join(hex_digits)
    result = result.lstrip('0')
    if not result:
        result = '0'
    return result

if __name__ == '__main__':
    print(binary_to_hex('101010'))
    print(binary_to_hex('11111111'))
    print(binary_to_hex('0'))