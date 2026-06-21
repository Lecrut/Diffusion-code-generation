def binary_to_hex_list(binary_strings: list) -> list:
    if not isinstance(binary_strings, list):
        raise TypeError('Input must be a list of strings.')
    result = []
    for binary_str in binary_strings:
        if not isinstance(binary_str, str):
            raise TypeError(f'Expected string, got {type(binary_str).__name__} for item {binary_str}')
        for char in binary_str:
            if char not in ('0', '1'):
                raise ValueError(f"Invalid binary character '{char}' in string '{binary_str}'")
        if binary_str == '':
            hex_val = '0X0'
        else:
            dec_val = int(binary_str, 2)
            hex_val = hex(dec_val).upper()
        result.append(hex_val)
    return result
if __name__ == '__main__':
    sample_binaries = ['1010', '11110000', '0', '1', '11111111', '0000']
    output = binary_to_hex_list(sample_binaries)
    print(output)