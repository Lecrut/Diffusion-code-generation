def binary_to_hex(binary_input):
    if not binary_input:
        return ""
    try:
        integer_value = int(binary_input, 2)
        return format(integer_value, 'x').upper()
    except ValueError:
        raise ValueError("Invalid binary input")

if __name__ == '__main__':
    sample_binary_values = ["1010", "11110000", "1010101010", "1111111111111111", "0", "1"]
    for sample in sample_binary_values:
        result = binary_to_hex(sample)
        print(result)