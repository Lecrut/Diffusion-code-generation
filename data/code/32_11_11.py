def binary_to_hex_list(binary_strings):
    valid_hex = []
    for b_str in binary_strings:
        if not all(c in '01' for c in b_str):
            raise ValueError(f"Invalid binary string: {b_str}")
        decimal_value = int(b_str, 2)
        hex_string = format(decimal_value, 'X')
        valid_hex.append(hex_string)
    return valid_hex

if __name__ == '__main__':
    sample_binary = ['1010', '11110000', '11011011', '00001111']
    result = binary_to_hex_list(sample_binary)
    print(result)