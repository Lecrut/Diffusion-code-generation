def binary_to_hex(binary_str):
    if not binary_str:
        return ''
    padding_needed = (4 - len(binary_str) % 4) % 4
    padded_binary = '0' * padding_needed + binary_str
    hex_chars = '0123456789ABCDEF'
    result = []
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i:i + 4]
        value = 0
        for bit in chunk:
            value = value << 1 | int(bit)
        result.append(hex_chars[value])
    return ''.join(result)
if __name__ == '__main__':
    sample_inputs = ['1010', '11110000', '00001111', '1101101011001011', '0', '0000', '1111111111111111']
    for binary_str in sample_inputs:
        hex_result = binary_to_hex(binary_str)
        print(hex_result)