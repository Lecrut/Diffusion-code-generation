def binary_to_hex(binary_string: str) -> str:
    if not all((c in '01' for c in binary_string)):
        raise ValueError("Input must be a binary string containing only '0' and '1'.")
    if not binary_string:
        return '0x0'
    decimal_value = int(binary_string, 2)
    return hex(decimal_value)
if __name__ == '__main__':
    test_cases = ['0', '1', '1010', '11110000', '1101111100001111', '1010101010101010']
    for binary in test_cases:
        result = binary_to_hex(binary)
        print(f'Binary: {binary} -> Hexadecimal: {result}')