BINARY_TO_HEX = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3',
    '0100': '4', '0101': '5', '0110': '6', '0111': '7',
    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
}

def binary_to_hex(binary_string):
    if not binary_string or len(binary_string) % 4 != 0:
        raise ValueError("Binary string length must be a multiple of 4")
    hex_parts = []
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i:i+4]
        if chunk not in BINARY_TO_HEX:
            raise ValueError(f"Invalid binary chunk: {chunk}")
        hex_parts.append(BINARY_TO_HEX[chunk])
    return ''.join(hex_parts)

if __name__ == '__main__':
    test_values = ['0000', '1010', '11110000', '110101101011']
    for val in test_values:
        result = binary_to_hex(val)
        print(f"{val} -> {result}")