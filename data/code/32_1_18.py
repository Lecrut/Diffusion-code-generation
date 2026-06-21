def binary_to_hex_list(binary_integers):
    result = []
    for num in binary_integers:
        hex_chars = []
        temp = num
        if temp == 0:
            hex_chars.append('0')
        else:
            while temp > 0:
                nibble = temp & 0xF
                if nibble < 10:
                    hex_chars.append(chr(ord('0') + nibble))
                else:
                    hex_chars.append(chr(ord('A') + (nibble - 10)))
                temp = temp >> 4
            hex_chars.reverse()
        result.append(''.join(hex_chars))
    return result

if __name__ == '__main__':
    sample_binary_integers = [0, 15, 255, 170, 42, 256, 1023]
    hex_strings = binary_to_hex_list(sample_binary_integers)
    print(hex_strings)