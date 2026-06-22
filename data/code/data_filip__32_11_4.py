def binary_strings_to_hex(binary_strings):
    hex_results = []
    for binary_str in binary_strings:
        if not all(c in '01' for c in binary_str):
            raise ValueError(f"Invalid binary string: {binary_str}")
        decimal_value = int(binary_str, 2)
        hex_str = format(decimal_value, 'X')
        hex_results.append(hex_str)
    return hex_results

if __name__ == '__main__':
    sample_binary_strings = ['1010', '1111', '1101', '1001']
    result = binary_strings_to_hex(sample_binary_strings)
    print(result)