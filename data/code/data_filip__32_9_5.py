def binary_to_hex(binary_input: str) -> str:
    if not binary_input:
        return '0x0'
    if not all((c in '01' for c in binary_input)):
        raise ValueError('Input must be a valid binary string containing only 0s and 1s.')
    decimal_value = int(binary_input, 2)
    hex_value = hex(decimal_value)
    return hex_value
if __name__ == '__main__':
    sample_binaries = ['0', '1', '1010', '1111', '1101011', '0000', '11111111']
    for binary_str in sample_binaries:
        result = binary_to_hex(binary_str)
        print(f'Binary: {binary_str} -> Hexadecimal: {result}')