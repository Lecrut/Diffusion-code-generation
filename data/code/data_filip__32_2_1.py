def binary_to_hex(binary_str: str) -> str:
    if not binary_str:
        raise ValueError("Input string cannot be empty")
    valid_chars = set('01')
    if not all(char in valid_chars for char in binary_str):
        raise ValueError("Input must contain only binary digits (0 and 1)")
    int_value = int(binary_str, 2)
    hex_value = format(int_value, 'X')
    return hex_value

if __name__ == '__main__':
    sample_binary_1 = "111100001010"
    sample_binary_2 = "1010101010101010"
    result_1 = binary_to_hex(sample_binary_1)
    result_2 = binary_to_hex(sample_binary_2)
    print(f"Binary: {sample_binary_1} -> Hex: {result_1}")
    print(f"Binary: {sample_binary_2} -> Hex: {result_2}")