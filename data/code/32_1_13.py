def binary_list_to_uppercase_hex(binary_list):
    def bits_to_int(bits):
        result = 0
        for bit in bits:
            result = (result << 1) | bit
        return result

    def int_to_hex_string(num):
        hex_chars = "0123456789ABCDEF"
        if num == 0:
            return "0"
        result = ""
        while num > 0:
            remainder = num & 15
            digit = hex_chars[remainder]
            result = digit + result
            num = num >> 4
        return result

    hex_strings = []
    for bits in binary_list:
        value = bits_to_int(bits)
        hex_val = int_to_hex_string(value)
        hex_strings.append(hex_val)
    return hex_strings

if __name__ == '__main__':
    sample_input = [[1, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
    output = binary_list_to_uppercase_hex(sample_input)
    print(output)