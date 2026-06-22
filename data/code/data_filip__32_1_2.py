def binary_list_to_hex(binary_list):
    if not binary_list:
        return []
    result = []
    for value in binary_list:
        if value < 0:
            hex_chars = []
            temp = -value
            while temp > 0:
                rem = temp & 15
                if rem < 10:
                    char_code = 48 + rem
                else:
                    char_code = 55 + rem
                hex_chars.append(chr(char_code))
                temp >>= 4
            if not hex_chars:
                hex_chars.append('0')
            hex_chars.reverse()
            result.append('-' + ''.join(hex_chars))
        else:
            if value == 0:
                result.append('0')
                continue
            hex_chars = []
            temp = value
            while temp > 0:
                rem = temp & 15
                if rem < 10:
                    char_code = 48 + rem
                else:
                    char_code = 55 + rem
                hex_chars.append(chr(char_code))
                temp >>= 4
            hex_chars.reverse()
            result.append(''.join(hex_chars))
    return result

if __name__ == '__main__':
    sample_values = [0, 1, 10, 15, 16, 255, 256, 4095, 4096, -5, -16]
    output = binary_list_to_hex(sample_values)
    print(output)