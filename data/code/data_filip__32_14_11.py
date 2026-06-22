def binary_to_hex(binary_string):
    if not binary_string:
        return "0"
    if not set(binary_string).issubset({'0', '1'}):
        raise ValueError("Input string must contain only '0' and '1' characters.")
    
    length = len(binary_string)
    padding = (4 - (length % 4)) % 4
    padded_binary = '0' * padding + binary_string
    
    hex_digits = []
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i : i + 4]
        val = (int(chunk[0]) << 3) + (int(chunk[1]) << 2) + (int(chunk[2]) << 1) + int(chunk[3])
        hex_digits.append(format(val, 'x'))
    
    return ''.join(hex_digits)

if __name__ == '__main__':
    sample_input = "11010110"
    result = binary_to_hex(sample_input)
    print(result)
    sample_input_large = "1" * 1000
    result_large = binary_to_hex(sample_input_large)
    print(len(result_large))