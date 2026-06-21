def binary_ints_to_hex_strings(binary_ints):
    result = []
    for num in binary_ints:
        hex_chars = []
        current = num
        while current > 0:
            nibble = current & 0xF
            if nibble < 10:
                hex_chars.append(chr(ord('0') + nibble))
            else:
                hex_chars.append(chr(ord('A') + (nibble - 10)))
            current >>= 4
        if not hex_chars:
            result.append('0')
        else:
            hex_chars.reverse()
            result.append(''.join(hex_chars))
    return result

if __name__ == '__main__':
    sample = [0, 15, 255, 16, 42, 256, 1023]
    print(binary_ints_to_hex_strings(sample))