def binary_to_hex(binary_string):
    if not binary_string:
        return ''
    padded_binary = binary_string.zfill((len(binary_string) + 3) // 4 * 4)
    bin_to_hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    hex_digits = []
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i:i + 4]
        hex_digits.append(bin_to_hex[chunk])
    return ''.join(hex_digits)
if __name__ == '__main__':
    sample_binary_1 = '11010110'
    sample_binary_2 = '101010101010'
    sample_binary_3 = '111100001111'
    sample_binary_4 = ''
    sample_binary_5 = '1'
    print(binary_to_hex(sample_binary_1))
    print(binary_to_hex(sample_binary_2))
    print(binary_to_hex(sample_binary_3))
    print(binary_to_hex(sample_binary_4))
    print(binary_to_hex(sample_binary_5))