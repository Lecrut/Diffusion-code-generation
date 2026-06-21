def binary_ints_to_hex_strings(binary_ints):
    hex_digits = '0123456789ABCDEF'
    results = []
    for num in binary_ints:
        if num == 0:
            results.append('0')
            continue
        hex_chars = []
        temp = num
        while temp > 0:
            remainder = temp & 0xF
            hex_chars.append(hex_digits[remainder])
            temp = temp >> 4
        hex_chars.reverse()
        results.append(''.join(hex_chars))
    return results

if __name__ == '__main__':
    sample_values = [0, 15, 16, 255, 100, 1023, 65535]
    print(binary_ints_to_hex_strings(sample_values))