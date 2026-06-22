def binary_to_hex(binary_input: str) -> str:
    binary_input = binary_input.strip()
    if not binary_input:
        raise ValueError("Input cannot be empty")
    if not all(c in '01' for c in binary_input):
        raise ValueError("Input contains non-binary characters")
    decimal_value = int(binary_input, 2)
    hex_output = hex(decimal_value)[2:].upper()
    return hex_output

if __name__ == '__main__':
    samples = [
        '0',
        '1',
        '1010',
        '11111111',
        '000011110000',
        '100000000'
    ]
    for sample in samples:
        result = binary_to_hex(sample)
        print(f"Binary: {sample} -> Hex: {result}")