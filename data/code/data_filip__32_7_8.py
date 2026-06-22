def binary_to_hex(binary_string):
    binary_list = [int(d) for d in binary_string]
    padding = len(binary_list) % 4
    if padding:
        binary_list = [0] * (4 - padding) + binary_list
    nibble_list = []
    for i in range(0, len(binary_list), 4):
        nibble = binary_list[i:i+4]
        val = sum(bit * (2 ** idx) for idx, bit in enumerate(reversed(nibble)))
        nibble_list.append(val)
    hex_digits = [hex(val)[2:].upper() for val in nibble_list]
    result = ''.join(hex_digits)
    return result

if __name__ == '__main__':
    binary_input = '110101101010'
    hex_result = binary_to_hex(binary_input)
    print(hex_result)