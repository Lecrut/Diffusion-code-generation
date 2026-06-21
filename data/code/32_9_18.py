def binary_to_hexadecimal(binary_input: str) -> str:
    cleaned = binary_input.replace(' ', '').replace(',', '')
    if not cleaned:
        return ''
    try:
        int_val = int(cleaned, 2)
    except ValueError:
        raise ValueError(f"Input '{binary_input}' contains invalid binary characters.")
    if int_val < 0:
        raise ValueError('Input must represent a non-negative integer.')
    hex_str = hex(int_val)[2:]
    return hex_str.upper()
if __name__ == '__main__':
    sample_binary = '111100001010'
    result = binary_to_hexadecimal(sample_binary)
    print(result)