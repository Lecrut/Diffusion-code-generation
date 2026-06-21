def binary_to_hex(binary_string):
    if not binary_string or all(char == '0' for char in binary_string):
        return "0"
    decimal_value = int(binary_string, 2)
    hex_string = format(decimal_value, 'X')
    return hex_string

if __name__ == '__main__':
    sample_inputs = ["1010", "11110000", "0000", "1", "0001010", "110011001100", "00000000001"]
    for sample in sample_inputs:
        result = binary_to_hex(sample)
        print(result)