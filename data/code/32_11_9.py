def binary_to_upper_hex(binary_strings):
    result = []
    for binary_string in binary_strings:
        if not all(c in '01' for c in binary_string):
            raise ValueError(f"Invalid binary string: {binary_string}")
        if len(binary_string) == 0:
            result.append("")
            continue
        decimal_value = int(binary_string, 2)
        hex_value = format(decimal_value, 'X')
        result.append(hex_value)
    return result

if __name__ == '__main__':
    sample_data = ["0000", "1010", "11111111", "10101010", "0", "1111", "10000", "11001100"]
    try:
        converted_values = binary_to_upper_hex(sample_data)
        for value in converted_values:
            print(value)
    except ValueError as e:
        print(f"Error: {e}")