def binary_to_hex(bin_strings):
    if not isinstance(bin_strings, list):
        raise TypeError("Input must be a list")
    result = []
    for binary_str in bin_strings:
        if not isinstance(binary_str, str):
            raise TypeError("Each element must be a string")
        if not all(c in '01' for c in binary_str):
            raise ValueError(f"Invalid binary string: {binary_str}")
        decimal_val = int(binary_str, 2)
        hex_str = format(decimal_val, 'X')
        result.append(hex_str)
    return result

if __name__ == '__main__':
    sample_binaries = [
        "1010",
        "11110000",
        "10101010",
        "11001100",
        "0",
        "1"
    ]
    hex_results = binary_to_hex(sample_binaries)
    print(hex_results)