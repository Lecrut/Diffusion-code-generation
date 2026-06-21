def binary_to_hex(binary_string):
    if len(binary_string) % 4 != 0:
        padding = 4 - (len(binary_string) % 4)
        binary_string = '0' * padding + binary_string
    groups = [binary_string[i:i+4] for i in range(0, len(binary_string), 4)]
    hex_values = [hex(int(group, 2))[2:] for group in groups]
    return ''.join(hex_values)

if __name__ == '__main__':
    sample_binary = '1101011010101111'
    result = binary_to_hex(sample_binary)
    print(result)