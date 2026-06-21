def binary_to_hexadecimal(binary_input):
    if not isinstance(binary_input, str):
        raise TypeError("Input must be a string")
    if not all(c in '01' for c in binary_input):
        raise ValueError("Input must contain only binary digits (0 and 1)")
    if not binary_input:
        return '0x0'
    padded_binary = binary_input.zfill((len(binary_input) + 3) // 4 * 4)
    decimal_value = int(padded_binary, 2)
    hex_string = format(decimal_value, 'X')
    return f"0x{hex_string}"

if __name__ == '__main__':
    sample_values = [
        "0",
        "1",
        "10101010",
        "11111111",
        "00000000",
        "1100110011001100"
    ]
    for sample in sample_values:
        print(binary_to_hexadecimal(sample))