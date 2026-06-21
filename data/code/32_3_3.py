BINARY_TO_HEX = {
    '0': '0', '1': '1', '2': '2', '3': '3',
    '4': '4', '5': '5', '6': '6', '7': '7',
    '8': '8', '9': '9', 'a': 'a', 'b': 'b',
    'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f',
    'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D',
    'E': 'E', 'F': 'F'
}

def binary_to_hex_map(binary_str: str) -> str:
    if not binary_str:
        return ''
    if len(binary_str) % 4 != 0:
        binary_str = '0' * (4 - (len(binary_str) % 4)) + binary_str
    hex_result = []
    for i in range(0, len(binary_str), 4):
        nibble = binary_str[i:i+4]
        val = int(nibble, 2)
        hex_result.append(BINARY_TO_HEX[str(val)])
    return ''.join(hex_result)

if __name__ == '__main__':
    sample1 = '1010'
    sample2 = '11110000'
    sample3 = '00001111'
    print(binary_to_hex_map(sample1))
    print(binary_to_hex_map(sample2))
    print(binary_to_hex_map(sample3))