BINARY_TO_HEX = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3',
    '0100': '4', '0101': '5', '0110': '6', '0111': '7',
    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
}

def binary_to_hex_string(binary_string):
    if not binary_string:
        return '0'
    padded_length = (len(binary_string) + 3) // 4 * 4
    padded_string = binary_string.zfill(padded_length)
    hex_chars = []
    for i in range(0, len(padded_string), 4):
        chunk = padded_string[i:i+4]
        if chunk not in BINARY_TO_HEX:
            raise ValueError(f"Invalid binary chunk: {chunk}")
        hex_chars.append(BINARY_TO_HEX[chunk])
    return ''.join(hex_chars).lstrip('0') or '0'

if __name__ == '__main__':
    sample_values = ['1111', '101010', '00001111', '1100110011001100']
    for val in sample_values:
        result = binary_to_hex_string(val)
        print(f"{val} -> {result}")