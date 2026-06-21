def binary_to_hex(binary_strings):
    results = []
    for b_str in binary_strings:
        for char in b_str:
            if char not in ('0', '1'):
                raise ValueError(f"Invalid binary character '{char}' in string '{b_str}'")
        if not b_str:
            raise ValueError("Empty binary string provided")
        decimal_value = int(b_str, 2)
        hex_value = format(decimal_value, 'X')
        results.append(hex_value)
    return results

if __name__ == '__main__':
    sample_data = ["0", "1", "10", "1111", "10101010", "1111000011110000"]
    output = binary_to_hex(sample_data)
    print(output)