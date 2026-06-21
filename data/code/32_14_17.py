def binary_string_to_hex(binary_str):
    if not binary_str:
        return ""
    if not all(c in '01' for c in binary_str):
        raise ValueError("Input must be a valid binary string containing only '0' and '1'")
    integer_value = int(binary_str, 2)
    hex_string = format(integer_value, 'X')
    return hex_string

if __name__ == '__main__':
    sample_input_1 = "111100001010"
    sample_input_2 = "10101010101010101010"
    sample_input_3 = "00001111"
    print(binary_string_to_hex(sample_input_1))
    print(binary_string_to_hex(sample_input_2))
    print(binary_string_to_hex(sample_input_3))