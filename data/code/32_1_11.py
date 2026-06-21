BIT_MASK = 0xF
HEX_MAP = {
    0: '0', 1: '1', 2: '2', 3: '3',
    4: '4', 5: '5', 6: '6', 7: '7',
    8: '8', 9: '9', 10: 'A', 11: 'B',
    12: 'C', 13: 'D', 14: 'E', 15: 'F'
}

def convert_to_hex(value):
    if value == 0:
        return '0'
    result = []
    temp = value
    while temp > 0:
        nibble = temp & BIT_MASK
        result.append(HEX_MAP[nibble])
        temp >>= 4
    return ''.join(reversed(result))

def process_binary_ints(binary_ints):
    return [convert_to_hex(n) for n in binary_ints]

if __name__ == '__main__':
    sample_values = [0, 1, 255, 16, 17, 128, 256, 4095, 4096, 65535]
    hex_results = process_binary_ints(sample_values)
    print(hex_results)