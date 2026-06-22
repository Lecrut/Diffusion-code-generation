def binary_to_hex(binary_string):
    if not binary_string:
        return "0"
    binary_string = binary_string.lstrip('0')
    if not binary_string:
        return "0"
    length = len(binary_string)
    padding = (4 - (length % 4)) % 4
    binary_string = '0' * padding + binary_string
    hex_digits = '0123456789ABCDEF'
    hex_result = []
    for i in range(0, len(binary_string), 4):
        nibble = binary_string[i:i+4]
        value = 0
        for char in nibble:
            value = (value << 1) | (1 if char == '1' else 0)
        hex_result.append(hex_digits[value])
    return ''.join(hex_result)

if __name__ == '__main__':
    sample_inputs = ["00000001", "1010", "0000", "111100001111", "1"]
    for s in sample_inputs:
        print(binary_to_hex(s))