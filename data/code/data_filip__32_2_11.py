def binary_to_hex(binary_input):
    if not isinstance(binary_input, str):
        raise TypeError("Input must be a string")
    if not all(c in '01' for c in binary_input):
        raise ValueError("Input must contain only '0' and '1'")
    if not binary_input:
        return "0"
    decimal_value = int(binary_input, 2)
    hex_string = hex(decimal_value)[2:]
    hex_string = hex_string.upper()
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string
    return hex_string

if __name__ == '__main__':
    sample_binaries = [
        "1010",
        "11110000",
        "1010101010101010",
        "0",
        "1",
        "1111111111111111",
        "10101010101010101010101010101010"
    ]
    for binary_str in sample_binaries:
        result = binary_to_hex(binary_str)
        print(result)