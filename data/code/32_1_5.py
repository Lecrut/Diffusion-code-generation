def binary_to_hex(binary_list):
    result = []
    for binary_int in binary_list:
        hex_chars = []
        temp = binary_int
        if temp == 0:
            result.append('0')
            continue
        while temp > 0:
            remainder = temp & 15
            if remainder < 10:
                hex_chars.append(chr(ord('0') + remainder))
            else:
                hex_chars.append(chr(ord('A') + remainder - 10))
            temp = temp >> 4
        result.append(''.join(reversed(hex_chars)))
    return result

if __name__ == '__main__':
    sample_data = [0, 15, 255, 16, 10, 2748]
    print(binary_to_hex(sample_data))