def binary_strings_to_hex(binary_strings):
    valid_chars = frozenset('01')
    results = []
    for binary_string in binary_strings:
        if not binary_string:
            raise ValueError("Empty binary string")
        for char in binary_string:
            if char not in valid_chars:
                raise ValueError(f"Invalid character '{char}' in binary string")
        decimal_value = int(binary_string, 2)
        hex_value = format(decimal_value, 'X')
        results.append(hex_value)
    return results

if __name__ == '__main__':
    sample_binary_strings = ['1010', '1111', '0000', '1001', '1100']
    result = binary_strings_to_hex(sample_binary_strings)
    print(result)