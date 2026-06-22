def binary_to_hex(binary_string):
    if not binary_string:
        raise ValueError("Input string cannot be empty")
    for char in binary_string:
        if char not in ('0', '1'):
            raise ValueError(f"Invalid binary character '{char}' found in input")
    decimal_value = int(binary_string, 2)
    return format(decimal_value, 'X')

if __name__ == '__main__':
    sample_binary_list = ["00001010", "11110000", "10101010", "0101", "11001100"]
    results = []
    for binary_str in sample_binary_list:
        hex_value = binary_to_hex(binary_str)
        results.append(hex_value)
    print(results)