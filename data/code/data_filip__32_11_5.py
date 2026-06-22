def binary_to_hex(binary_strings):
    result = []
    for binary in binary_strings:
        try:
            int_value = int(binary, 2)
            hex_value = hex(int_value)[2:].upper()
            result.append(hex_value)
        except ValueError:
            raise ValueError(f"Invalid binary string: {binary}")
    return result

if __name__ == '__main__':
    sample_binary_list = ["00001111", "10101010", "11110000", "01010101", "111111111111"]
    print(binary_to_hex(sample_binary_list))