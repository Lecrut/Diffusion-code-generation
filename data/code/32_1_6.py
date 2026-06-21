def binary_ints_to_hex_strings(binary_ints):
    result = []
    for number in binary_ints:
        hex_chars = []
        temp = number
        if temp == 0:
            hex_chars.append('0')
        while temp > 0:
            nibble = temp & 0xF
            temp = temp >> 4
            if nibble < 10:
                hex_chars.append(chr(ord('0') + nibble))
            else:
                hex_chars.append(chr(ord('A') + (nibble - 10)))
        hex_chars.reverse()
        result.append(''.join(hex_chars))
    return result

if __name__ == '__main__':
    sample = [0, 10, 255, 16, 42]
    print(binary_ints_to_hex_strings(sample))