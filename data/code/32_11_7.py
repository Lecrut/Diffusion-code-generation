def binary_to_hex(binary_strings):
    results = []
    for s in binary_strings:
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        if len(s) == 0:
            raise ValueError("Binary string cannot be empty")
        for char in s:
            if char not in ('0', '1'):
                raise ValueError(f"Invalid binary character '{char}' in string '{s}'")
        hex_val = format(int(s, 2), 'X')
        results.append(hex_val)
    return results

if __name__ == '__main__':
    binary_data = ['1010', '11111111', '100000000000', '0', '111']
    output = binary_to_hex(binary_data)
    print(output)