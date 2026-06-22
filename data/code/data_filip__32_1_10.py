def binary_list_to_hex(binary_list):
    hex_result = []
    for value in binary_list:
        hex_str = ''
        temp_val = value
        if temp_val == 0:
            hex_str = '0'
        else:
            hex_chars = '0123456789ABCDEF'
            while temp_val > 0:
                remainder = temp_val & 15
                digit = hex_chars[remainder]
                hex_str = digit + hex_str
                temp_val >>= 4
        hex_result.append(hex_str)
    return hex_result

if __name__ == '__main__':
    sample_binaries = [0, 10, 255, 2748, 4095]
    print(binary_list_to_hex(sample_binaries))