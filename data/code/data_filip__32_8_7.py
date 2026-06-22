def binary_to_hex(binary_string):
    if not binary_string:
        return '0'
    binary_string = binary_string.lstrip('0')
    if not binary_string:
        return '0'
    padding = (4 - len(binary_string) % 4) % 4
    padded_binary = '0' * padding + binary_string
    hex_digits = '0123456789ABCDEF'
    hex_string = ''
    for i in range(0, len(padded_binary), 4):
        nibble = padded_binary[i:i+4]
        value = 0
        for j, bit in enumerate(reversed(nibble)):
            if bit == '1':
                value += 2 ** j
        hex_string += hex_digits[value]
    return hex_string

if __name__ == '__main__':
    test_cases = ['1111', '10101010', '0000', '0011110000111100', '1']
    for case in test_cases:
        print(binary_to_hex(case))