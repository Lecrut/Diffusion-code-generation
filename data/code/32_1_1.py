def binary_ints_to_hex_strings(binary_ints):
    hex_strings = []
    for num in binary_ints:
        hex_chars = []
        temp = num
        while temp > 0:
            nibble = temp & 0xF
            temp >>= 4
            if nibble < 10:
                hex_chars.append(chr(ord('0') + nibble))
            else:
                hex_chars.append(chr(ord('A') + (nibble - 10)))
        if not hex_chars:
            hex_chars.append('0')
        hex_strings.append(''.join(reversed(hex_chars)))
    return hex_strings

if __name__ == '__main__':
    sample_values = [0, 1, 255, 16, 17, 128, 256, 4095, 4096, 65535]
    result = binary_ints_to_hex_strings(sample_values)
    print(result)