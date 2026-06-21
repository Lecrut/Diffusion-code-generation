def binary_to_hex_list(binary_strings):
    hex_results = []
    for binary_str in binary_strings:
        if not all(c in '01' for c in binary_str):
            raise ValueError(f"Invalid binary string: {binary_str}")
        decimal_value = int(binary_str, 2)
        hex_value = format(decimal_value, 'X')
        hex_results.append(hex_value)
    return hex_results

if __name__ == '__main__':
    sample_binaries = ['1010', '1101', '1111', '1000']
    result = binary_to_hex_list(sample_binaries)
    print(result)