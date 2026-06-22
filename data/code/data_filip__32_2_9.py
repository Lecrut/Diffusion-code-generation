def binary_to_hexadecimal(binary_input):
    if not isinstance(binary_input, str):
        raise TypeError("Input must be a string")
    binary_input = binary_input.strip()
    if not binary_input:
        return "0"
    valid_chars = set('01')
    if not all(c in valid_chars for c in binary_input):
        raise ValueError("Input contains invalid binary digits")
    integer_value = int(binary_input, 2)
    hex_value = hex(integer_value)[2:].upper()
    return hex_value

if __name__ == '__main__':
    sample_values = ["0", "1", "1010", "11110000", "0000", "101010101010"]
    for sample in sample_values:
        print(binary_to_hexadecimal(sample))