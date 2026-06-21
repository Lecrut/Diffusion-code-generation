def validate_and_convert_binary_to_hex(binary_str):
    if not isinstance(binary_str, str):
        raise ValueError("Input must be a string")
    for char in binary_str:
        if char not in ('0', '1'):
            raise ValueError(f"Invalid binary character: {char}")
    decimal_value = int(binary_str, 2)
    return hex(decimal_value)

if __name__ == '__main__':
    sample_inputs = ['1010', '1111', '0000', '10010101', '']
    for sample in sample_inputs:
        result = validate_and_convert_binary_to_hex(sample)
        print(result)
    invalid_samples = ['102', 'abc', '10101 0011', '10.01']
    for invalid_sample in invalid_samples:
        try:
            validate_and_convert_binary_to_hex(invalid_sample)
        except ValueError as e:
            print(e)