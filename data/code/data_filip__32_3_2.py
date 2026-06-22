BINARY_TO_HEX = {
    '0': '0', '1': '1', '2': '2', '3': '3',
    '4': '4', '5': '5', '6': '6', '7': '7',
    '8': '8', '9': '9', 'a': 'A', 'b': 'B',
    'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
    'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D',
    'E': 'E', 'F': 'F', '0000': '0', '0001': '1',
    '0010': '2', '0011': '3', '0100': '4', '0101': '5',
    '0110': '6', '0111': '7', '1000': '8', '1001': '9',
    '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D',
    '1110': 'E', '1111': 'F'
}

def binary_to_hex_string(binary_str: str) -> str:
    if not binary_str:
        return ''
    binary_str = binary_str.replace(' ', '')
    if any(c not in '01' for c in binary_str):
        raise ValueError("Input must contain only 0s and 1s")
    length = len(binary_str)
    padding = (4 - length % 4) % 4
    padded_str = '0' * padding + binary_str
    result = []
    for i in range(0, len(padded_str), 4):
        chunk = padded_str[i:i+4]
        result.append(BINARY_TO_HEX[chunk])
    return ''.join(result)

def hex_digit_lookup(bit_0: str, bit_1: str, bit_2: str, bit_3: str) -> str:
    key = bit_0 + bit_1 + bit_2 + bit_3
    if key not in BINARY_TO_HEX:
        raise ValueError("Invalid binary digits provided")
    return BINARY_TO_HEX[key]

if __name__ == '__main__':
    sample_binary = '110101101011'
    converted_value = binary_to_hex_string(sample_binary)
    print(converted_value)
    single_hex = hex_digit_lookup('1', '1', '0', '1')
    print(single_hex)