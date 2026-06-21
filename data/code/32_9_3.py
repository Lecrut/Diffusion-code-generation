def binary_to_hex(binary_input: str) -> str:
    if not binary_input:
        raise ValueError('Binary input cannot be empty')
    if not all((c in '01' for c in binary_input)):
        raise ValueError('Binary input contains invalid characters')
    decimal_value = int(binary_input, 2)
    return hex(decimal_value)
if __name__ == '__main__':
    samples = ['0', '1', '1010', '11110000', '1101101110', '1111111111111111']
    for sample in samples:
        result = binary_to_hex(sample)
        print(result)