def binary_to_hex(bitwise_integers):
    hex_strings = []
    for num in bitwise_integers:
        hex_digits = "0123456789ABCDEF"
        if num == 0:
            hex_strings.append("0")
            continue
        temp = num
        result = ""
        while temp > 0:
            nibble = temp & 0xF
            result = hex_digits[nibble] + result
            temp = temp >> 4
        hex_strings.append(result)
    return hex_strings

if __name__ == '__main__':
    sample_values = [0, 1, 15, 255, 16, 42, 256, 1024, 65535]
    result = binary_to_hex(sample_values)
    print(result)