def binary_to_hex(binary_string):
    padding = (4 - len(binary_string) % 4) % 4
    padded_string = binary_string.zfill(len(binary_string) + padding)
    hex_digits = '0123456789ABCDEF'
    hex_result = []
    for i in range(0, len(padded_string), 4):
        chunk = padded_string[i:i+4]
        value = 0
        for bit in chunk:
            value = (value << 1) | int(bit)
        hex_result.append(hex_digits[value])
    return ''.join(hex_result)

if __name__ == '__main__':
    sample_binary = '110101110010'
    print(binary_to_hex(sample_binary))